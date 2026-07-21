"""Intermediate representation (IR) shared by every code emitter.

`spec.py` builds an `Api` graph from the vendored OpenAPI document; `emit_python.py` and
`emit_csharp.py` (a later phase) render it into each target language. This module is the
contract between the two sides — field names and shapes here must not change without
updating every emitter that reads them.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TypeRef:
    """A reference to a value's type, resolved from a JSON Schema fragment.

    `kind` is one of: 'string', 'int', 'number', 'bool', 'datetime', 'object', 'any',
    'array', 'model', 'enum'. `model` carries the PascalCase model/enum name when
    `kind` is 'model' or 'enum'. `item` carries the element type when `kind` is 'array'.
    """

    kind: str
    model: str | None = None
    item: "TypeRef | None" = None


@dataclass
class EnumType:
    """A named enumeration with its wire (string) values, in spec order."""

    name: str
    values: list[str]
    doc: str = ""


@dataclass
class Field:
    """A single property of a `Model`."""

    py_name: str
    cs_name: str
    wire_name: str
    type: TypeRef
    required: bool = False
    read_only: bool = False
    doc: str = ""


@dataclass
class Model:
    """A generated type corresponding to one named component schema."""

    name: str
    fields: list[Field] = field(default_factory=list)
    doc: str = ""


@dataclass
class Param:
    """A path or query parameter of an `Operation`."""

    py_name: str
    cs_name: str
    wire_name: str
    location: str
    type: TypeRef
    required: bool = False
    doc: str = ""


@dataclass
class Operation:
    """One API operation (a single HTTP method on a single path)."""

    operation_id: str
    py_name: str
    cs_name: str
    http_method: str
    path: str
    path_params: list[Param] = field(default_factory=list)
    query_params: list[Param] = field(default_factory=list)
    body_type: TypeRef | None = None
    body_required: bool = False
    is_multipart: bool = False
    return_type: TypeRef | None = None
    tag: str = ""
    summary: str = ""
    doc: str = ""


@dataclass
class Api:
    """The complete IR for the GetResponse API: every model, enum, and operation."""

    models: list[Model] = field(default_factory=list)
    enums: list[EnumType] = field(default_factory=list)
    operations: list[Operation] = field(default_factory=list)
