"""Foundation tests: naming helpers, spec transforms, and a full build against the
real vendored spec.
"""

from __future__ import annotations

from codegen.ir import EnumType, Model
from codegen.naming import (
    camel_case,
    pascal_case,
    safe_cs_ident,
    safe_py_ident,
    snake_case,
)
from codegen.spec import build_api, load

# --------------------------------------------------------------------------------
# naming
# --------------------------------------------------------------------------------


def test_snake_case_camel_to_snake():
    assert snake_case("getContactList") == "get_contact_list"
    assert snake_case("campaignId") == "campaign_id"
    assert snake_case("createdOn") == "created_on"


def test_pascal_case():
    assert pascal_case("from-fields") == "FromFields"
    assert pascal_case("getContactList") == "GetContactList"


def test_camel_case():
    assert camel_case("CampaignId") == "campaignId"
    assert camel_case("from-fields") == "fromFields"


def test_safe_py_ident_reserved_word():
    assert safe_py_ident("from").endswith("_")
    assert safe_py_ident("class").endswith("_")
    assert safe_py_ident("normal_name") == "normal_name"


def test_safe_cs_ident_reserved_word():
    assert safe_cs_ident("class").endswith("_")
    assert safe_cs_ident("namespace").endswith("_")
    assert safe_cs_ident("normalName") == "normalName"


def test_safe_ident_leading_digit():
    assert safe_py_ident("2fa").startswith("_")
    assert safe_cs_ident("2fa").startswith("_")


# --------------------------------------------------------------------------------
# allOf flattening
# --------------------------------------------------------------------------------


def _tiny_spec_with_allof() -> dict:
    return {
        "openapi": "3.0.0",
        "info": {"title": "t", "version": "1"},
        "paths": {},
        "components": {
            "schemas": {
                "Base": {
                    "type": "object",
                    "properties": {
                        "createdOn": {"type": "string", "format": "date-time"},
                    },
                },
                "Extended": {
                    "type": "object",
                    "allOf": [{"$ref": "#/components/schemas/Base"}],
                    "properties": {
                        "name": {"type": "string"},
                    },
                },
            }
        },
    }


def test_allof_flatten_merges_base_and_own_properties():
    api = build_api(_tiny_spec_with_allof())
    models = {m.name: m for m in api.models}
    assert "Extended" in models
    extended = models["Extended"]
    field_names = {f.wire_name for f in extended.fields}
    assert "createdOn" in field_names
    assert "name" in field_names
    # Base itself also qualifies as its own model.
    assert "Base" in models


# --------------------------------------------------------------------------------
# enums
# --------------------------------------------------------------------------------


def _tiny_spec_with_enum() -> dict:
    return {
        "openapi": "3.0.0",
        "info": {"title": "t", "version": "1"},
        "paths": {},
        "components": {
            "schemas": {
                "StatusEnum": {
                    "type": "string",
                    "enum": ["active", "inactive"],
                    "description": "The status.",
                },
                "Thing": {
                    "type": "object",
                    "properties": {
                        "status": {"$ref": "#/components/schemas/StatusEnum"},
                    },
                },
            }
        },
    }


def test_named_enum_schema_produces_enum_type():
    api = build_api(_tiny_spec_with_enum())
    enums = {e.name: e for e in api.enums}
    assert "StatusEnum" in enums
    status = enums["StatusEnum"]
    assert isinstance(status, EnumType)
    assert status.values == ["active", "inactive"]

    thing = next(m for m in api.models if m.name == "Thing")
    status_field = next(f for f in thing.fields if f.wire_name == "status")
    assert status_field.type.kind == "enum"
    assert status_field.type.model == "StatusEnum"


# --------------------------------------------------------------------------------
# real vendored spec
# --------------------------------------------------------------------------------


def test_build_api_on_real_spec():
    api = build_api(load())

    assert len(api.operations) == 220
    assert len(api.models) >= 300
    assert isinstance(api.models[0], Model)

    op_ids = [op.operation_id for op in api.operations]
    assert len(op_ids) == len(set(op_ids)), "operationIds must be unique"

    for op in api.operations:
        assert op.tag, f"operation {op.operation_id} has no tag"
        assert op.py_name, f"operation {op.operation_id} has no py_name"
