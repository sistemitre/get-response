"""Load the vendored OpenAPI spec and transform it into the `Api` IR.

The heavy lifting is JSON-Schema-to-`TypeRef` resolution (`_Builder._resolve_type` /
`_resolve_named_ref`), `allOf` flattening (`_flatten_allof`), and turning `paths` into
`Operation`s (`_Builder._build_operation`). See `ir.py` for the target shapes and the
project `CLAUDE.md` / plan for the design rationale.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from codegen.ir import Api, EnumType, Field, Model, Operation, Param, TypeRef
from codegen.naming import (
    camel_case,
    pascal_case,
    safe_cs_ident,
    safe_py_ident,
    snake_case,
)

_DEFAULT_SPEC_PATH = "openapi/open-api.json"
_HTTP_METHODS = ("get", "post", "put", "patch", "delete")
_SUCCESS_CODES = ("200", "201")

_WHITESPACE = re.compile(r"\s+")


def load(path: str | Path = _DEFAULT_SPEC_PATH) -> dict[str, Any]:
    """Load and parse the vendored OpenAPI JSON document."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)  # type: ignore[no-any-return]


def _normalize_doc(text: str | None) -> str:
    """Collapse whitespace/newlines from a spec description into one clean sentence."""
    return _WHITESPACE.sub(" ", text or "").strip()


def _flatten_bracket_name(wire_name: str) -> str:
    """Turn a bracket-notation wire name into an underscore-joined token string.

    `'query[createdOn][from]'` -> `'query_createdOn_from'`.
    """
    return wire_name.replace("[", "_").replace("]", "")


def _flatten_allof(schema: dict[str, Any], schemas: dict[str, Any]) -> dict[str, Any]:
    """Recursively merge an `allOf` chain's `properties`/`required` into one flat set.

    Subschemas are merged in order, then the schema's own (non-`allOf`) properties are
    applied last, so later/own keys override earlier/inherited ones.
    """
    properties: dict[str, Any] = {}
    required: set[str] = set()
    for sub in schema.get("allOf", []):
        if "$ref" in sub:
            sub = schemas[sub["$ref"].split("/")[-1]]
        merged = _flatten_allof(sub, schemas)
        properties.update(merged["properties"])
        required |= merged["required"]
    properties.update(schema.get("properties", {}))
    required |= set(schema.get("required", []))
    return {
        "properties": properties,
        "required": required,
        "description": schema.get("description", ""),
    }


def _is_model_worthy(schema: dict[str, Any], schemas: dict[str, Any]) -> bool:
    """A named schema becomes a `Model` only if it resolves to an object with fields.

    Free-form objects (no properties, e.g. `additionalProperties`-only maps) and
    oneOf/anyOf unions are represented as the permissive `object` `TypeRef` instead.
    """
    if "oneOf" in schema or "anyOf" in schema:
        return False
    return bool(_flatten_allof(schema, schemas)["properties"])


class _Builder:
    """Holds the mutable state needed while walking the spec into an `Api`."""

    def __init__(self, spec: dict[str, Any]) -> None:
        self.spec = spec
        self.schemas: dict[str, Any] = spec.get("components", {}).get("schemas", {})
        self.api = Api()
        self.models_by_name: dict[str, Model] = {}
        self.enums_by_name: dict[str, EnumType] = {}

    # -- models & enums -----------------------------------------------------------

    def build_models_and_enums(self) -> None:
        """Pass 1: register every qualifying named schema as a `Model` or `EnumType`.

        Registering up front (before resolving any field types) lets `$ref`s between
        component schemas - including self- and mutually-recursive ones - resolve to a
        `TypeRef` without needing recursion guards.
        """
        for name, schema in self.schemas.items():
            if "oneOf" in schema or "anyOf" in schema:
                continue
            if "enum" in schema and "allOf" not in schema:
                enum_type = EnumType(
                    name=name,
                    values=list(schema["enum"]),
                    doc=_normalize_doc(schema.get("description")),
                )
                self.enums_by_name[name] = enum_type
                self.api.enums.append(enum_type)
            elif _is_model_worthy(schema, self.schemas):
                model = Model(name=name, doc="")
                self.models_by_name[name] = model
                self.api.models.append(model)

        # Pass 2: now that every model/enum name is known, fill in each model's fields
        # (which may themselves reference other models/enums, or register new inline
        # enums discovered along the way).
        for name, model in self.models_by_name.items():
            schema = self.schemas[name]
            flat = _flatten_allof(schema, self.schemas)
            model.doc = _normalize_doc(flat["description"] or schema.get("description"))
            for wire_name, prop_schema in flat["properties"].items():
                model.fields.append(
                    self._build_field(name, wire_name, prop_schema, flat["required"])
                )

    def _build_field(
        self,
        model_name: str,
        wire_name: str,
        prop_schema: dict[str, Any],
        required: set[str],
    ) -> Field:
        field_pascal = pascal_case(_flatten_bracket_name(wire_name))
        type_ref = self._resolve_type(
            prop_schema, ctx_name=f"{model_name}{field_pascal}"
        )
        return Field(
            py_name=safe_py_ident(snake_case(wire_name)),
            cs_name=safe_cs_ident(pascal_case(wire_name)),
            wire_name=wire_name,
            type=type_ref,
            required=wire_name in required,
            read_only=bool(prop_schema.get("readOnly", False)),
            doc=_normalize_doc(prop_schema.get("description")),
        )

    def _register_enum(self, name: str, values: list[str], doc: str) -> str:
        """Register an inline enum, disambiguating a name collision with a numeric suffix.

        Returns the name actually registered under (may differ from `name` on collision).
        """
        existing = self.enums_by_name.get(name)
        if existing is None:
            key = name
        elif existing.values == values:
            return name
        else:
            i = 2
            key = f"{name}{i}"
            while (
                key in self.enums_by_name and self.enums_by_name[key].values != values
            ):
                i += 1
                key = f"{name}{i}"
            if key in self.enums_by_name and self.enums_by_name[key].values == values:
                return key
        enum_type = EnumType(name=key, values=list(values), doc=doc)
        self.enums_by_name[key] = enum_type
        self.api.enums.append(enum_type)
        return key

    # -- type resolution ------------------------------------------------------------

    def _resolve_type(self, schema: dict[str, Any] | None, ctx_name: str) -> TypeRef:
        """Resolve one JSON Schema fragment (inline or `$ref`) into a `TypeRef`.

        `ctx_name` seeds the generated name for an inline enum encountered here, e.g.
        `f"{ModelName}{FieldPascal}"` from `_build_field`.
        """
        if not schema:
            return TypeRef(kind="any")
        if "$ref" in schema:
            ref_name = schema["$ref"].split("/")[-1]
            return self._resolve_named_ref(ref_name)
        if "oneOf" in schema or "anyOf" in schema:
            return self._resolve_union(schema.get("oneOf") or schema["anyOf"], ctx_name)
        if "enum" in schema:
            name = self._register_enum(
                ctx_name, schema["enum"], _normalize_doc(schema.get("description"))
            )
            return TypeRef(kind="enum", model=name)
        return self._resolve_scalar_or_array(schema, ctx_name)

    def _resolve_union(self, branches: list[dict[str, Any]], ctx_name: str) -> TypeRef:
        """Resolve a `oneOf`/`anyOf` list of branches."""
        resolved = []
        for b in branches:
            if not isinstance(b, dict) or ("$ref" in b or "enum" in b or "oneOf" in b or "anyOf" in b):
                return TypeRef(kind="object")
            resolved.append(self._resolve_scalar_or_array(b, ctx_name))
        kinds = {r.kind for r in resolved}
        if len(kinds) == 1 and resolved[0].kind not in ("object", "any"):
            return resolved[0]
        return TypeRef(kind="object")

    def _resolve_named_ref(self, ref_name: str) -> TypeRef:
        """Resolve a `$ref` to a component schema, using pre-registered models/enums."""
        if ref_name in self.models_by_name:
            return TypeRef(kind="model", model=ref_name)
        if ref_name in self.enums_by_name:
            return TypeRef(kind="enum", model=ref_name)
        target = self.schemas[ref_name]
        if "oneOf" in target or "anyOf" in target:
            return self._resolve_union(target.get("oneOf") or target["anyOf"], ref_name)
        # A named schema that isn't a registered model/enum: a bare scalar or array
        # alias (e.g. a component schema that is just `{"type": "string"}`), or a
        # free-form object. Resolve it structurally without registering a model.
        return self._resolve_scalar_or_array(target, ref_name)

    def _resolve_scalar_or_array(
        self, schema: dict[str, Any], ctx_name: str
    ) -> TypeRef:
        json_type = schema.get("type")
        if json_type == "array":
            item = self._resolve_type(
                schema.get("items", {}), ctx_name=f"{ctx_name}Item"
            )
            return TypeRef(kind="array", item=item)
        if json_type == "string":
            fmt = schema.get("format")
            if fmt in ("date-time", "date"):
                return TypeRef(kind="datetime")
            return TypeRef(kind="string")
        if json_type == "integer":
            return TypeRef(kind="int")
        if json_type == "number":
            return TypeRef(kind="number")
        if json_type == "boolean":
            return TypeRef(kind="bool")
        if json_type == "object":
            return TypeRef(kind="object")
        return TypeRef(kind="any")

    # -- operations -------------------------------------------------------------

    def build_operations(self) -> None:
        """Pass 3: walk `paths` into `Operation`s (path/query params, body, response)."""
        for path, path_item in self.spec.get("paths", {}).items():
            shared_params = path_item.get("parameters", [])
            for method in _HTTP_METHODS:
                op = path_item.get(method)
                if op is None:
                    continue
                self.api.operations.append(
                    self._build_operation(path, method, op, shared_params)
                )

    def _resolve_param(self, param_obj: dict[str, Any]) -> dict[str, Any]:
        if "$ref" in param_obj:
            name = param_obj["$ref"].split("/")[-1]
            return self.spec["components"]["parameters"][name]  # type: ignore[no-any-return]
        return param_obj

    def _build_param(self, param_obj: dict[str, Any], op_ctx: str) -> Param:
        resolved = self._resolve_param(param_obj)
        wire_name = resolved["name"]
        flat_name = _flatten_bracket_name(wire_name)
        field_pascal = pascal_case(flat_name)
        type_ref = self._resolve_type(
            resolved.get("schema", {}), ctx_name=f"{op_ctx}{field_pascal}"
        )
        return Param(
            py_name=safe_py_ident(snake_case(flat_name)),
            cs_name=safe_cs_ident(camel_case(flat_name)),
            wire_name=wire_name,
            location=resolved["in"],
            type=type_ref,
            required=bool(resolved.get("required", False)),
            doc=_normalize_doc(resolved.get("description")),
        )

    def _resolve_request_body(
        self, rb: dict[str, Any] | None, op_ctx: str
    ) -> tuple[TypeRef | None, bool, bool]:
        """Return `(body_type, body_required, is_multipart)` for an operation's body."""
        if rb is None:
            return None, False, False
        if "$ref" in rb:
            name = rb["$ref"].split("/")[-1]
            target = self.spec["components"]["requestBodies"][name]
        else:
            target = rb
        required = bool(target.get("required", False))
        content = target.get("content", {})
        if "multipart/form-data" in content:
            return TypeRef(kind="object"), required, True
        if "application/json" in content:
            schema = content["application/json"].get("schema", {})
            return self._resolve_type(schema, ctx_name=f"{op_ctx}Body"), required, False
        return None, required, False

    def _resolve_response(
        self, responses: dict[str, Any], op_ctx: str
    ) -> TypeRef | None:
        """Return the `TypeRef` for the first 200/201 response with a JSON body, if any."""
        for code in _SUCCESS_CODES:
            resp = responses.get(code)
            if resp is None:
                continue
            if "$ref" in resp:
                name = resp["$ref"].split("/")[-1]
                target = self.spec["components"]["responses"][name]
            else:
                target = resp
            content = target.get("content", {})
            if "application/json" in content:
                schema = content["application/json"].get("schema", {})
                return self._resolve_type(schema, ctx_name=f"{op_ctx}Response")
        return None

    def _build_operation(
        self,
        path: str,
        method: str,
        op: dict[str, Any],
        shared_params: list[dict[str, Any]],
    ) -> Operation:
        operation_id = op["operationId"]
        op_ctx = pascal_case(operation_id)

        path_params: list[Param] = []
        query_params: list[Param] = []
        for param_obj in [*shared_params, *op.get("parameters", [])]:
            param = self._build_param(param_obj, op_ctx)
            if param.location == "path":
                path_params.append(param)
            else:
                query_params.append(param)

        body_type, body_required, is_multipart = self._resolve_request_body(
            op.get("requestBody"), op_ctx
        )
        return_type = self._resolve_response(op.get("responses", {}), op_ctx)

        tags = op.get("tags", [])
        summary = _normalize_doc(op.get("summary"))
        description = _normalize_doc(op.get("description"))

        return Operation(
            operation_id=operation_id,
            py_name=snake_case(operation_id),
            cs_name=f"{pascal_case(operation_id)}Async",
            http_method=method.upper(),
            path=path,
            path_params=path_params,
            query_params=query_params,
            body_type=body_type,
            body_required=body_required,
            is_multipart=is_multipart,
            return_type=return_type,
            tag=tags[0] if tags else "",
            summary=summary,
            doc=description or summary,
        )


def build_api(spec: dict[str, Any]) -> Api:
    """Transform a parsed OpenAPI document into the full `Api` IR."""
    builder = _Builder(spec)
    builder.build_models_and_enums()
    builder.build_operations()
    return builder.api
