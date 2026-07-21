"""Identifier case conversion and reserved-word sanitization.

The spec uses camelCase (and occasionally kebab-case) for property names, operationIds,
and parameter names. These helpers turn those into idiomatic Python (snake_case) and C#
(PascalCase / camelCase) identifiers, and guard against language reserved words.
"""

from __future__ import annotations

import keyword
import re

# Boundary before an uppercase letter that follows a lowercase letter or digit:
# "getContactList" -> "get_Contact_List", "campaignId" -> "campaign_Id".
_LOWER_TO_UPPER = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")

# Boundary inside an acronym run, before the last uppercase letter that starts a new
# word: "SMSMessage" -> "SMS_Message", "fromURLValue" -> "from_URL_Value".
_ACRONYM_BOUNDARY = re.compile(r"(?<=[A-Z])(?=[A-Z][a-z])")

# Any run of characters that aren't letters/digits (spaces, hyphens, slashes, ...).
_NON_ALNUM = re.compile(r"[^0-9a-zA-Z]+")


def _words(s: str) -> list[str]:
    """Split an identifier of any case style into lowercase word tokens."""
    s = _NON_ALNUM.sub("_", s)
    s = _LOWER_TO_UPPER.sub("_", s)
    s = _ACRONYM_BOUNDARY.sub("_", s)
    return [w.lower() for w in s.split("_") if w]


def snake_case(s: str) -> str:
    """Convert camelCase/PascalCase/kebab-case to snake_case.

    >>> snake_case("getContactList")
    'get_contact_list'
    >>> snake_case("campaignId")
    'campaign_id'
    """
    return "_".join(_words(s))


def pascal_case(s: str) -> str:
    """Convert any case style to PascalCase.

    >>> pascal_case("from-fields")
    'FromFields'
    >>> pascal_case("getContactList")
    'GetContactList'
    """
    return "".join(w.capitalize() for w in _words(s))


def camel_case(s: str) -> str:
    """Convert any case style to camelCase (used for C# method parameters).

    >>> camel_case("CampaignId")
    'campaignId'
    """
    pascal = pascal_case(s)
    if not pascal:
        return pascal
    return pascal[0].lower() + pascal[1:]


# Python keywords/soft-keywords plus a few builtins that shadow badly as field/param
# names in generated code.
_PY_RESERVED = set(keyword.kwlist) | set(keyword.softkwlist) | {"self", "cls"}

# C# reserved keywords (contextual keywords like `var`/`async` are intentionally
# excluded since they remain valid identifiers).
_CS_RESERVED = {
    "abstract",
    "as",
    "base",
    "bool",
    "break",
    "byte",
    "case",
    "catch",
    "char",
    "checked",
    "class",
    "const",
    "continue",
    "decimal",
    "default",
    "delegate",
    "do",
    "double",
    "else",
    "enum",
    "event",
    "explicit",
    "extern",
    "false",
    "finally",
    "fixed",
    "float",
    "for",
    "foreach",
    "goto",
    "if",
    "implicit",
    "in",
    "int",
    "interface",
    "internal",
    "is",
    "lock",
    "long",
    "namespace",
    "new",
    "null",
    "object",
    "operator",
    "out",
    "override",
    "params",
    "private",
    "protected",
    "public",
    "readonly",
    "ref",
    "return",
    "sbyte",
    "sealed",
    "short",
    "sizeof",
    "stackalloc",
    "static",
    "string",
    "struct",
    "switch",
    "this",
    "throw",
    "true",
    "try",
    "typeof",
    "uint",
    "ulong",
    "unchecked",
    "unsafe",
    "ushort",
    "using",
    "virtual",
    "void",
    "volatile",
    "while",
}


def safe_py_ident(s: str) -> str:
    """Return `s` as a valid, non-reserved Python identifier.

    Appends a trailing underscore for reserved words (`from` -> `from_`); prefixes an
    underscore if the name would otherwise start with a digit.
    """
    if s and s[0].isdigit():
        s = f"_{s}"
    if s in _PY_RESERVED:
        s = f"{s}_"
    return s


def safe_cs_ident(s: str) -> str:
    """Return `s` as a valid, non-reserved C# identifier.

    Appends a trailing underscore for reserved words (`class` -> `class_`); prefixes an
    underscore if the name would otherwise start with a digit.
    """
    if s and s[0].isdigit():
        s = f"_{s}"
    if s in _CS_RESERVED:
        s = f"{s}_"
    return s
