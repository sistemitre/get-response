"""Python emitter: renders the `Api` IR into the `get-response-py` package.

This is the only place Python source text gets generated. Every embedded string literal
(doc comments, wire names, aliases) is produced via `repr()` so we never hand-roll quote
escaping; `emit()` finishes by running `ruff format` + `ruff check --fix` over the output,
which normalizes quote style and prunes any imports a given module ends up not needing.

Do not hand-edit `get-response-py/` -- fix this module and regenerate instead.
"""

from __future__ import annotations

import keyword
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pydantic

from codegen.ir import Api, EnumType, Model, Operation, Param, TypeRef

# -- shared helpers ------------------------------------------------------------------

_WORD_RE = re.compile(r"[0-9a-zA-Z]+")

# Attributes pydantic.BaseModel already defines (model_dump, copy, json, ...): a field
# whose Python name collides with one of these gets an underscore appended so it doesn't
# shadow inherited behavior. The wire alias is untouched, so the JSON shape is unaffected.
_BASEMODEL_ATTRS = set(dir(pydantic.BaseModel))


def _lit(value: str) -> str:
    """Render `value` as a safe Python string literal (used for docstrings/aliases)."""
    return repr(value)


def _py_type(t: TypeRef) -> str:
    """Map a `TypeRef` to the Python type annotation (and runtime-valid expression) for it."""
    if t.kind == "string":
        return "str"
    if t.kind == "int":
        return "int"
    if t.kind == "number":
        return "float"
    if t.kind == "bool":
        return "bool"
    if t.kind == "datetime":
        return "datetime"
    if t.kind == "object":
        return "dict[str, Any]"
    if t.kind == "any":
        return "Any"
    if t.kind == "array":
        assert t.item is not None
        return f"list[{_py_type(t.item)}]"
    if t.kind in ("model", "enum"):
        assert t.model is not None
        return t.model
    raise ValueError(f"unhandled TypeRef kind: {t.kind!r}")


def _collect_names(t: TypeRef | None, out: set[str]) -> None:
    """Gather every model/enum class name referenced by `t`, recursing into arrays."""
    if t is None:
        return
    if t.kind == "array":
        _collect_names(t.item, out)
    elif t.kind in ("model", "enum"):
        assert t.model is not None
        out.add(t.model)


def _enum_member_name(value: str, used: set[str]) -> str:
    """Turn an enum wire value into a valid, unique Python identifier for a member name.

    >>> _enum_member_name("text/html", set())
    'TextHtml'
    >>> _enum_member_name("12h", set())
    'V_12h'
    """
    words = _WORD_RE.findall(value)
    name = "".join(w.capitalize() for w in words) if words else "EMPTY"
    if name[0].isdigit():
        name = f"V_{name}"
    if keyword.iskeyword(name):
        name = f"{name}_"
    base, i = name, 2
    while name in used:
        name = f"{base}_{i}"
        i += 1
    used.add(name)
    return name


def _tag_words(tag: str) -> list[str]:
    """Split a tag into word tokens, treating `/` as a non-boundary (so `A/B` -> `AB`)."""
    return _WORD_RE.findall(tag.replace("/", ""))


def _tag_pascal(tag: str) -> str:
    """`'A/B tests - subject'` -> `'AbTestsSubject'`, `'SMS Messages'` -> `'SmsMessages'`."""
    return "".join(w.capitalize() for w in _tag_words(tag))


def _tag_snake(tag: str) -> str:
    """`'A/B tests - subject'` -> `'ab_tests_subject'`."""
    return "_".join(w.lower() for w in _tag_words(tag))


def _py_field_name(py_name: str) -> str:
    """Rename a field that would otherwise shadow a `BaseModel` attribute (e.g. `copy`)."""
    return f"{py_name}_" if py_name in _BASEMODEL_ATTRS else py_name


def _dedupe_by_wire_name(params: list[Param]) -> list[Param]:
    """Drop duplicate params sharing a wire name (the spec occasionally repeats a path

    parameter both at the path-item level and the operation level).
    """
    seen: set[str] = set()
    out = []
    for p in params:
        if p.wire_name not in seen:
            seen.add(p.wire_name)
            out.append(p)
    return out


# -- models.py -------------------------------------------------------------------------


def _render_enum(e: EnumType) -> str:
    lines = [f"class {e.name}(str, Enum):"]
    lines.append(f"    {_lit(e.doc or f'{e.name} enum.')}")
    lines.append("")
    used: set[str] = set()
    for v in e.values:
        member = _enum_member_name(v, used)
        lines.append(f"    {member} = {_lit(v)}")
    return "\n".join(lines)


def _render_model(m: Model) -> str:
    lines = [f"class {m.name}(BaseModel):"]
    lines.append(f"    {_lit(m.doc or f'{m.name} model.')}")
    lines.append("")
    lines.append('    model_config = ConfigDict(populate_by_name=True, extra="ignore")')
    if not m.fields:
        return "\n".join(lines)
    lines.append("")
    for f in m.fields:
        ann = _py_type(f.type)
        py_name = _py_field_name(f.py_name)
        if f.required:
            ann_full = ann
            default = f"Field(alias={_lit(f.wire_name)})"
        else:
            ann_full = f"{ann} | None"
            default = f"Field(default=None, alias={_lit(f.wire_name)})"
        lines.append(f"    {py_name}: {ann_full} = {default}")
        if f.doc:
            lines.append(f"    {_lit(f.doc)}")
    return "\n".join(lines)


def _render_models_py(api: Api) -> str:
    enums_sorted = sorted(api.enums, key=lambda e: e.name)
    models_sorted = sorted(api.models, key=lambda m: m.name)

    parts = [
        '"""Generated data models: every schema in the GetResponse OpenAPI spec.\n\n'
        'Enums come first (models may reference them), then models in name order. This\n'
        'file is generated -- do not edit it directly.\n"""',
        "",
        "from __future__ import annotations",
        "",
        "from datetime import datetime",
        "from enum import Enum",
        "from typing import Any",
        "",
        "from pydantic import BaseModel, ConfigDict, Field",
        "",
    ]
    for e in enums_sorted:
        parts.append("")
        parts.append(_render_enum(e))
    for m in models_sorted:
        parts.append("")
        parts.append(_render_model(m))

    parts.append("")
    parts.append("")
    parts.append(
        "# Every model above is now defined, so cross-references (including forward and\n"
        "# self-references) can be resolved in one pass.\n"
        "for _model_cls in list(globals().values()):\n"
        "    if (\n"
        "        isinstance(_model_cls, type)\n"
        "        and issubclass(_model_cls, BaseModel)\n"
        "        and _model_cls is not BaseModel\n"
        "    ):\n"
        "        _model_cls.model_rebuild(force=True)"
    )
    return "\n".join(parts) + "\n"


# -- resources/*.py ----------------------------------------------------------------


def _render_multipart_method(op: Operation) -> str:
    return_ann = _py_type(op.return_type) if op.return_type is not None else "None"
    doc = f"{op.doc or op.summary or op.operation_id} Sends `file` as multipart/form-data."
    return "\n".join(
        [
            f"    async def {op.py_name}(self, *, file: bytes, filename: str = "
            f'"upload") -> {return_ann}:',
            f"        {_lit(doc)}",
            "        return await self._core.request(",
            f"            {_lit(op.http_method)},",
            f"            {_lit(op.path)},",
            '            files={"file": (filename, file)},',
            f"            return_type={return_ann},",
            "        )",
        ]
    )


def _render_method(op: Operation) -> str:
    if op.is_multipart:
        return _render_multipart_method(op)

    path_params = _dedupe_by_wire_name(op.path_params)
    query_params = _dedupe_by_wire_name(op.query_params)

    sig = ["self"]
    for p in path_params:
        sig.append(f"{p.py_name}: str")

    body_param = "body" if op.body_type is not None else None
    if body_param:
        assert op.body_type is not None
        sig.append(f"body: {_py_type(op.body_type)}")

    if query_params:
        sig.append("*")
        for p in sorted(query_params, key=lambda p: p.required, reverse=True):
            ann = _py_type(p.type)
            sig.append(f"{p.py_name}: {ann}" if p.required else f"{p.py_name}: {ann} | None = None")

    return_ann = _py_type(op.return_type) if op.return_type is not None else "None"
    doc = op.doc or op.summary or op.operation_id

    path_expr = (
        "{" + ", ".join(f"{_lit(p.wire_name)}: {p.py_name}" for p in path_params) + "}"
        if path_params
        else "None"
    )
    query_expr = (
        "{" + ", ".join(f"{_lit(p.wire_name)}: {p.py_name}" for p in query_params) + "}"
        if query_params
        else "None"
    )
    return_type_expr = return_ann if op.return_type is not None else "None"

    return "\n".join(
        [
            f"    async def {op.py_name}({', '.join(sig)}) -> {return_ann}:",
            f"        {_lit(doc)}",
            "        return await self._core.request(",
            f"            {_lit(op.http_method)},",
            f"            {_lit(op.path)},",
            f"            path_params={path_expr},",
            f"            query={query_expr},",
            f"            body={body_param or 'None'},",
            f"            return_type={return_type_expr},",
            "        )",
        ]
    )


def _render_resource_module(tag: str, ops: list[Operation]) -> str:
    class_name = f"{_tag_pascal(tag)}Resource"
    referenced: set[str] = set()
    for op in ops:
        for p in (*op.path_params, *op.query_params):
            _collect_names(p.type, referenced)
        _collect_names(op.body_type, referenced)
        _collect_names(op.return_type, referenced)

    doc = f"Operations tagged {tag!r} in the GetResponse API."

    parts = [
        f'"""{doc}"""',
        "",
        "from __future__ import annotations",
        "",
        "from datetime import datetime",
        "from typing import Any",
        "",
        "from .._core import _Core",
    ]
    if referenced:
        if len(referenced) == 1:
            parts.append(f"from ..models import {next(iter(referenced))}")
        else:
            parts.append("from ..models import (")
            parts.extend(f"    {name}," for name in sorted(referenced))
            parts.append(")")
    parts.append("")
    parts.append("")
    parts.append(f"class {class_name}:")
    parts.append(f"    {_lit(doc)}")
    parts.append("")
    parts.append("    def __init__(self, core: _Core) -> None:")
    parts.append("        self._core = core")
    for op in sorted(ops, key=lambda o: o.py_name):
        parts.append("")
        parts.append(_render_method(op))
    return "\n".join(parts) + "\n"


def _render_resources_init(tags: list[str]) -> str:
    lines = ['"""Resource-group clients, one per API tag."""', ""]
    for tag in tags:
        lines.append(f"from .{_tag_snake(tag)} import {_tag_pascal(tag)}Resource")
    lines.append("")
    lines.append("__all__ = [")
    lines.extend(f'    "{_tag_pascal(tag)}Resource",' for tag in tags)
    lines.append("]")
    return "\n".join(lines) + "\n"


# -- client.py, _core.py, __init__.py, py.typed -----------------------------------


def _render_resource_groups_py(tags: list[str]) -> str:
    """Render `_resource_groups.py`: a mixin adding one typed resource attribute per tag.

    `client.py` is scaffold-once (hand-maintained after first creation), but the set of
    resource groups is spec-derived and must stay in sync as tags are added/removed. This
    mixin is the always-regenerated half: `GetResponseClient(_ResourceGroups)` gets the
    attributes/typing for free, and `_attach_resource_groups` does the assignment that used
    to live inline in the client's `__init__`.
    """
    lines = [
        '"""Resource-group attributes attached to GetResponseClient. Generated from the '
        'spec\'s tags."""',
        "",
        "from __future__ import annotations",
        "",
        "from ._core import _Core",
        "from .resources import (",
    ]
    lines.extend(f"    {_tag_pascal(tag)}Resource," for tag in tags)
    lines.append(")")
    lines.append("")
    lines.append("")
    lines.append("class _ResourceGroups:")
    lines.append('    """Mixin providing one typed resource-group attribute per API tag."""')
    lines.append("")
    for tag in tags:
        lines.append(f"    {_tag_snake(tag)}: {_tag_pascal(tag)}Resource")
    lines.append("")
    lines.append("    def _attach_resource_groups(self, core: _Core) -> None:")
    for tag in tags:
        lines.append(f"        self.{_tag_snake(tag)} = {_tag_pascal(tag)}Resource(core)")
    return "\n".join(lines) + "\n"


_CLIENT_PY = '''"""Root async client: auth, resource groups, lifecycle, and pagination."""

from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Callable
from typing import Any

import httpx

from ._core import DEFAULT_BASE_URL, _Core
from ._ratelimit import RateLimitOptions
from ._resource_groups import _ResourceGroups


class GetResponseClient(_ResourceGroups):
    """Async GetResponse v3 API client; one resource-group attribute per tag."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        access_token: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 30.0,
        transport: httpx.AsyncBaseTransport | None = None,
        rate_limit: RateLimitOptions | None = None,
    ) -> None:
        if (api_key is None) == (access_token is None):
            raise ValueError("Provide exactly one of `api_key` or `access_token`.")
        headers = (
            {"X-Auth-Token": f"api-key {api_key}"}
            if api_key is not None
            else {"Authorization": f"Bearer {access_token}"}
        )
        self._client = httpx.AsyncClient(
            base_url=base_url, headers=headers, timeout=timeout, transport=transport
        )
        self._core = _Core(self._client, rate_limit)
        self._attach_resource_groups(self._core)

    async def aclose(self) -> None:
        """Close the underlying HTTP connection pool."""
        await self._client.aclose()

    async def __aenter__(self) -> GetResponseClient:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: object | None,
    ) -> None:
        await self.aclose()

    async def paginate(
        self,
        list_method: Callable[..., Awaitable[list[Any]]],
        *,
        per_page: int = 100,
        **kwargs: Any,
    ) -> AsyncIterator[Any]:
        """Walk every page of a `list_*` resource method, yielding items one by one.

        GetResponse also reports `TotalCount`/`CurrentPage`/`TotalPages` response
        headers, but resource methods only return typed bodies (no header access),
        so this walks by page length instead: it stops once a page comes back empty
        or shorter than `per_page`.
        """
        page = 1
        while True:
            items = await list_method(page=page, per_page=per_page, **kwargs)
            if not items:
                return
            for item in items:
                yield item
            if len(items) < per_page:
                return
            page += 1
'''


_RATELIMIT_PY = '''"""Opt-in rate limiter: a concurrency cap plus per-second/per-window token buckets.

Disabled unless a `RateLimitOptions` is passed to `GetResponseClient(rate_limit=...)`. `_Core`
owns one `_RateLimiter` per client and drives it around every send attempt: `acquire()` before
sending (a concurrency slot, an rps token, a window token, and any adaptive block from a prior
response), `release()` after, and `observe()`/`reset_seconds_from()` to read the response's rate
headers. Every wait is capped by `max_wait`; exceeding it raises `_WaitExceedsMaxWait`, which
`_Core` turns into the public `RateLimitError`.
"""

from __future__ import annotations

import asyncio
import re
import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Any

import httpx

_RESET_RE = re.compile(r"\\d+")


def _parse_reset_seconds(value: str) -> int | None:
    """Extract the leading integer from a header value like `"432 seconds"`."""
    m = _RESET_RE.search(value)
    return int(m.group()) if m else None


async def _default_sleep(seconds: float) -> None:
    """Default `RateLimitOptions.sleep`: real `asyncio.sleep`, overridable in tests."""
    await asyncio.sleep(seconds)


def _default_clock() -> float:
    """Default `RateLimitOptions.clock`: real monotonic time, overridable in tests."""
    return time.monotonic()


@dataclass
class RateLimitOptions:
    """Opt-in rate-limit tuning; pass to `GetResponseClient(rate_limit=...)` to enable it.

    `safety_margin` (range `(0, 1]`) scales `requests_per_second`/`requests_per_window` down
    before they're used as bucket capacities -- concurrency is never scaled. `sleep`/`clock`
    are injectable so tests can run against a fake, instantly-advancing clock.
    """

    enabled: bool = True
    max_concurrency: int = 10
    requests_per_second: float = 80
    requests_per_window: float = 30000
    window_seconds: float = 600
    safety_margin: float = 1.0
    max_retries: int = 5
    max_wait: float = 60.0
    sleep: Callable[[float], Awaitable[None]] = _default_sleep
    clock: Callable[[], float] = _default_clock

    @property
    def effective_rps(self) -> float:
        """`requests_per_second` scaled by `safety_margin` and floored."""
        return float(int(self.requests_per_second * self.safety_margin))

    @property
    def effective_rpw(self) -> float:
        """`requests_per_window` scaled by `safety_margin` and floored."""
        return float(int(self.requests_per_window * self.safety_margin))


class _WaitExceedsMaxWait(Exception):
    """Internal signal: a proactive wait would exceed `max_wait`; `_Core` maps this to `RateLimitError`."""

    def __init__(self, wait_seconds: float) -> None:
        self.wait_seconds = wait_seconds
        super().__init__(f"wait of {wait_seconds:.1f}s exceeds max_wait")


class _TokenBucket:
    """Continuous-refill token bucket: `capacity` tokens, refilling at `rate` tokens/second."""

    def __init__(self, rate: float, capacity: float, *, clock: Callable[[], float]) -> None:
        self._rate = rate
        self._capacity = capacity
        self._clock = clock
        self._tokens = capacity
        self._last = clock()

    def _refill(self) -> None:
        now = self._clock()
        self._tokens = min(self._capacity, self._tokens + (now - self._last) * self._rate)
        self._last = now

    def wait_time(self) -> float:
        """Seconds until one token is available (0 if one already is). Does not consume it."""
        self._refill()
        if self._tokens >= 1 or self._rate <= 0:
            return 0.0
        return (1 - self._tokens) / self._rate

    def consume(self) -> None:
        """Take one token. Call only right after waiting out `wait_time()`."""
        self._refill()
        self._tokens -= 1


class _RateLimiter:
    """Per-client rate limiter: wraps every send attempt with proactive and adaptive throttling."""

    def __init__(self, options: RateLimitOptions) -> None:
        self.options = options
        self._concurrency = asyncio.Semaphore(options.max_concurrency)
        self._rps_bucket = _TokenBucket(
            options.effective_rps, options.effective_rps, clock=options.clock
        )
        self._rpw_bucket = _TokenBucket(
            options.effective_rpw / options.window_seconds,
            options.effective_rpw,
            clock=options.clock,
        )
        self._blocked_until: float | None = None

    async def acquire(self) -> None:
        """Take a concurrency slot, then wait out whichever of rps/window/adaptive-block is

        longest. Raises `_WaitExceedsMaxWait` instead of waiting past `options.max_wait`; on
        that path the concurrency slot is released again before raising.
        """
        await self._concurrency.acquire()
        try:
            wait = 0.0
            if self._blocked_until is not None:
                remaining = self._blocked_until - self.options.clock()
                if remaining <= 0:
                    self._blocked_until = None
                else:
                    wait = remaining
            wait = max(wait, self._rps_bucket.wait_time(), self._rpw_bucket.wait_time())
            if wait > self.options.max_wait:
                raise _WaitExceedsMaxWait(wait)
            if wait > 0:
                await self.options.sleep(wait)
            self._rps_bucket.consume()
            self._rpw_bucket.consume()
        except Exception:
            self._concurrency.release()
            raise

    def release(self) -> None:
        """Free the concurrency slot taken by a matching `acquire()`."""
        self._concurrency.release()

    def observe(self, headers: httpx.Headers) -> None:
        """Adaptive best-effort throttle: block new requests once a response reports 0 left."""
        remaining = headers.get("X-RateLimit-Remaining")
        if remaining is None:
            return
        try:
            if int(remaining) > 0:
                return
        except ValueError:
            return
        reset = self.reset_seconds_from(headers, None)
        wait = reset if reset is not None else self.options.window_seconds
        self._blocked_until = self.options.clock() + wait

    def reset_seconds_from(
        self, headers: httpx.Headers, context: dict[str, Any] | None
    ) -> float | None:
        """Seconds until the limit resets: the `X-RateLimit-Reset` header, else

        `context["timeToReset"]` (from a parsed `ErrorResponse`).
        """
        header_value = headers.get("X-RateLimit-Reset")
        if header_value is not None:
            parsed = _parse_reset_seconds(header_value)
            if parsed is not None:
                return float(parsed)
        if context and context.get("timeToReset") is not None:
            try:
                return float(context["timeToReset"])
            except (TypeError, ValueError):
                return None
        return None
'''

_CORE_PY = '''"""HTTP transport: request building, auth-agnostic call plumbing, and error mapping."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

import httpx
from pydantic import BaseModel, TypeAdapter

from ._ratelimit import RateLimitOptions, _RateLimiter, _WaitExceedsMaxWait
from .models import ErrorResponse

DEFAULT_BASE_URL = "https://api.getresponse.com/v3"
MAX_US_BASE_URL = "https://api3.getresponse360.com/v3"
MAX_PL_BASE_URL = "https://api3.getresponse360.pl/v3"


class GetResponseApiError(Exception):
    """Raised for any non-2xx response; carries the parsed `ErrorResponse` fields."""

    def __init__(
        self,
        status_code: int,
        *,
        code: int | None = None,
        code_description: str | None = None,
        message: str | None = None,
        more_info: str | None = None,
        context: dict[str, Any] | None = None,
        uuid: str | None = None,
    ) -> None:
        self.status_code = status_code
        self.code = code
        self.code_description = code_description
        self.message = message
        self.more_info = more_info
        self.context = context
        self.uuid = uuid
        super().__init__(
            f"GetResponse API error {status_code}: {message or code_description or 'unknown error'}"
        )

    @classmethod
    def from_response(cls, response: httpx.Response) -> GetResponseApiError:
        """Build from an HTTP error response, tolerating a body that isn't an `ErrorResponse`."""
        try:
            err = ErrorResponse.model_validate(response.json())
        except Exception:
            return cls(status_code=response.status_code, message=response.text or None)
        return cls(
            status_code=response.status_code,
            code=err.code,
            code_description=err.code_description,
            message=err.message,
            more_info=err.more_info,
            context=err.context,
            uuid=err.uuid,
        )


class RateLimitError(GetResponseApiError):
    """Raised by the rate limiter: retries after a 429 were exhausted, or a wait -- proactive

    (concurrency slot / token bucket / adaptive block) or reactive (429 reset) -- would exceed
    `RateLimitOptions.max_wait`.
    """

    def __init__(
        self,
        status_code: int = 429,
        *,
        code: int | None = None,
        code_description: str | None = None,
        message: str | None = None,
        more_info: str | None = None,
        context: dict[str, Any] | None = None,
        uuid: str | None = None,
        reset_seconds: float | None = None,
        limit: int | None = None,
        remaining: int | None = None,
    ) -> None:
        super().__init__(
            status_code,
            code=code,
            code_description=code_description,
            message=message,
            more_info=more_info,
            context=context,
            uuid=uuid,
        )
        self.reset_seconds = reset_seconds
        self.limit = limit
        self.remaining = remaining

    @classmethod
    def from_error(
        cls,
        err: GetResponseApiError,
        *,
        reset_seconds: float | None,
        limit: int | None,
        remaining: int | None,
    ) -> RateLimitError:
        """Attach rate-limit fields to a `GetResponseApiError` already parsed from a 429."""
        return cls(
            err.status_code,
            code=err.code,
            code_description=err.code_description,
            message=err.message,
            more_info=err.more_info,
            context=err.context,
            uuid=err.uuid,
            reset_seconds=reset_seconds,
            limit=limit,
            remaining=remaining,
        )

    @classmethod
    def wait_too_long(cls, wait_seconds: float) -> RateLimitError:
        """Build for a proactive wait that would exceed `max_wait` (no HTTP response involved)."""
        return cls(
            429,
            message=f"rate limit wait of {wait_seconds:.1f}s exceeds max_wait",
            reset_seconds=wait_seconds,
        )


def _int_or_none(value: str | None) -> int | None:
    """Parse an optional header string as an int, tolerating a missing/invalid value."""
    if value is None:
        return None
    try:
        return int(value)
    except ValueError:
        return None


def _encode_query(query: dict[str, Any] | None) -> dict[str, Any] | None:
    """Drop `None` values; encode enums/datetimes/bools to their wire representation."""
    if not query:
        return None
    encoded: dict[str, Any] = {}
    for key, value in query.items():
        if value is None:
            continue
        if isinstance(value, Enum):
            encoded[key] = value.value
        elif isinstance(value, datetime):
            encoded[key] = value.isoformat()
        elif isinstance(value, bool):
            encoded[key] = "true" if value else "false"
        else:
            encoded[key] = value
    return encoded


class _Core:
    """Thin wrapper around an `httpx.AsyncClient`: one call site for every operation."""

    def __init__(
        self, client: httpx.AsyncClient, rate_limit: RateLimitOptions | None = None
    ) -> None:
        self._client = client
        self._limiter = (
            _RateLimiter(rate_limit) if rate_limit is not None and rate_limit.enabled else None
        )

    async def request(
        self,
        method: str,
        path: str,
        *,
        path_params: dict[str, str] | None = None,
        query: dict[str, Any] | None = None,
        body: Any = None,
        files: dict[str, Any] | None = None,
        return_type: Any = None,
    ) -> Any:
        """Send one API call and decode the response into `return_type` (or `None`)."""
        url = path.format(**(path_params or {}))
        params = _encode_query(query)
        json_body: Any = None
        if isinstance(body, BaseModel):
            json_body = body.model_dump(mode="json", by_alias=True, exclude_none=True)
        elif body is not None:
            json_body = body

        response = await self._send(method, url, params, json_body, files)
        if response.status_code >= 400:
            raise GetResponseApiError.from_response(response)
        if return_type is None or response.status_code == 204 or not response.content:
            return None
        return TypeAdapter(return_type).validate_python(response.json())

    async def _send(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None,
        json_body: Any,
        files: dict[str, Any] | None,
    ) -> httpx.Response:
        """Send the request as-is when no limiter is configured (zero overhead, unchanged

        behavior); otherwise run it through the limiter's proactive acquire and reactive
        429-retry loop.
        """
        if self._limiter is None:
            return await self._client.request(method, url, params=params, json=json_body, files=files)

        attempt = 0
        while True:
            try:
                await self._limiter.acquire()
            except _WaitExceedsMaxWait as exc:
                raise RateLimitError.wait_too_long(exc.wait_seconds) from exc
            try:
                response = await self._client.request(
                    method, url, params=params, json=json_body, files=files
                )
            finally:
                self._limiter.release()
            self._limiter.observe(response.headers)
            if response.status_code != 429:
                return response

            attempt += 1
            err = GetResponseApiError.from_response(response)
            reset = self._limiter.reset_seconds_from(response.headers, err.context)
            opts = self._limiter.options
            if attempt < opts.max_retries and reset is not None and reset <= opts.max_wait:
                await opts.sleep(reset)
                continue
            raise RateLimitError.from_error(
                err,
                reset_seconds=reset,
                limit=_int_or_none(response.headers.get("X-RateLimit-Limit")),
                remaining=_int_or_none(response.headers.get("X-RateLimit-Remaining")),
            )
'''

_INIT_PY = '''"""Async, fully-typed GetResponse v3 API client."""

from . import models
from ._core import GetResponseApiError, RateLimitError
from ._ratelimit import RateLimitOptions
from .client import GetResponseClient

__all__ = [
    "GetResponseClient",
    "GetResponseApiError",
    "RateLimitError",
    "RateLimitOptions",
    "models",
]
'''

_PYPROJECT_TOML = '''[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "getresponse"
version = "0.1.0"
description = "Async, fully-typed Python client for the GetResponse v3 API."
readme = "README.md"
requires-python = ">=3.10"
license = { text = "MIT" }
authors = [{ name = "Sistemi Tre" }]
dependencies = [
    "httpx>=0.27",
    "pydantic>=2",
]

[project.urls]
Repository = "https://github.com/sistemitre/get-response"
Issues = "https://github.com/sistemitre/get-response/issues"

[project.optional-dependencies]
dev = [
    "pytest",
    "pytest-asyncio",
    "ruff",
    "mypy",
]

[tool.hatch.build.targets.wheel]
packages = ["getresponse"]

[tool.ruff]
line-length = 100
target-version = "py310"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B", "SIM"]
ignore = ["E501"]

[tool.pytest.ini_options]
asyncio_mode = "auto"

[tool.mypy]
python_version = "3.10"
check_untyped_defs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_return_any = false
'''

_README_MD = '''# getresponse

An async, fully-typed Python client for the [GetResponse v3 API](https://apireference.getresponse.com/),
generated from the official OpenAPI spec.

## Install

```bash
pip install -e .
```

## Quickstart

```python
import asyncio

from getresponse import GetResponseClient


async def main() -> None:
    async with GetResponseClient(api_key="YOUR_API_KEY") as client:
        contacts = await client.contacts.get_contact_list(query_email="jane@example.com")
        for contact in contacts:
            print(contact.contact_id, contact.email)


asyncio.run(main())
```

Use `access_token=` instead of `api_key=` to authenticate with an OAuth2 bearer token.

A real API key (or access token) is required for live use; the test suite mocks the
network entirely and needs neither.

## Pagination

Resource `list_*`/`get_*_list` methods return one page at a time. `GetResponseClient.paginate`
walks every page for you:

```python
async for contact in client.paginate(client.contacts.get_contact_list, per_page=100):
    print(contact.email)
```

It stops once a page comes back empty or shorter than `per_page` -- simpler and more
transport-agnostic than reading the `TotalPages`/`CurrentPage` response headers.

## Rate limiting

The client can throttle itself to stay under GetResponse's API limits. It's **opt-in** --
pass `rate_limit=` and it's off by default:

```python
from getresponse import GetResponseClient, RateLimitOptions

client = GetResponseClient(
    api_key="YOUR_API_KEY",
    rate_limit=RateLimitOptions(safety_margin=0.9),
)
```

When enabled, every request goes through:

- **Proactive throttling**: a concurrency cap (`max_concurrency`, default 10) plus per-second
  and per-window token buckets (`requests_per_second`/`requests_per_window`, default 80 and
  30000 over `window_seconds`, default 600). `safety_margin` (default `1.0`) scales the rps/
  window caps down before use; concurrency is never scaled.
- **Reactive retries**: on an HTTP 429, the reset time is read from the `X-RateLimit-Reset`
  header (falling back to the error body's `context.timeToReset`) and the request is retried
  after sleeping that long, up to `max_retries` (default 5).
- **Adaptive best-effort throttling**: `X-RateLimit-Remaining`/`X-RateLimit-Limit` response
  headers are tracked, and new requests are blocked once a response reports zero remaining.

Every wait -- proactive or reactive -- is capped by `max_wait` (default 60s). If satisfying a
request would require waiting longer than that, the client raises `RateLimitError` (a
`GetResponseApiError` subclass with `reset_seconds`/`limit`/`remaining`) instead of sleeping
indefinitely.

Note: GetResponse's limits are enforced per account/API key on their side. If the same key is
shared across multiple client instances or processes, each instance only tracks its own
requests, so the actual server-side limit can still be hit -- this limiter is a best-effort,
client-local approximation, not a substitute for a shared/coordinated limiter.

'''

# -- tests --------------------------------------------------------------------------

_TEST_CONFTEST = '''"""Shared pytest fixtures: build a `GetResponseClient` over a mocked HTTP transport."""

from __future__ import annotations

from collections.abc import Callable

import httpx

from getresponse import GetResponseClient


def make_client(
    handler: Callable[[httpx.Request], httpx.Response], *, api_key: str = "test-key"
) -> GetResponseClient:
    """Build a client whose requests are served entirely by `handler` (no real network)."""
    return GetResponseClient(api_key=api_key, transport=httpx.MockTransport(handler))
'''

_TEST_AUTH = '''"""Auth header selection: `X-Auth-Token` for API keys, `Bearer` for OAuth2 tokens."""

from __future__ import annotations

import httpx
import pytest

from getresponse import GetResponseClient


async def test_api_key_sends_x_auth_token_header() -> None:
    captured: dict[str, httpx.Headers] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["headers"] = request.headers
        return httpx.Response(200, json=[])

    async with GetResponseClient(api_key="my-key", transport=httpx.MockTransport(handler)) as c:
        await c.contacts.get_contact_list()

    assert captured["headers"]["X-Auth-Token"] == "api-key my-key"


async def test_access_token_sends_bearer_header() -> None:
    captured: dict[str, httpx.Headers] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["headers"] = request.headers
        return httpx.Response(200, json=[])

    async with GetResponseClient(
        access_token="my-token", transport=httpx.MockTransport(handler)
    ) as c:
        await c.contacts.get_contact_list()

    assert captured["headers"]["Authorization"] == "Bearer my-token"


def test_requires_exactly_one_credential() -> None:
    with pytest.raises(ValueError):
        GetResponseClient()
    with pytest.raises(ValueError):
        GetResponseClient(api_key="a", access_token="b")
'''

_TEST_QUERY_BUILDING = '''"""Bracket-notation query parameter building."""

from __future__ import annotations

import httpx

from getresponse import GetResponseClient


async def test_query_params_use_bracket_notation_and_skip_none() -> None:
    captured: dict[str, httpx.URL] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["url"] = request.url
        return httpx.Response(200, json=[])

    async with GetResponseClient(api_key="k", transport=httpx.MockTransport(handler)) as c:
        await c.contacts.get_contact_list(
            query_email="a@b.com", sort_name="asc", page=2, per_page=50
        )

    params = captured["url"].params
    assert params["query[email]"] == "a@b.com"
    assert params["sort[name]"] == "asc"
    assert params["page"] == "2"
    assert params["perPage"] == "50"
    assert "query[name]" not in params
'''

_TEST_MODELS = '''"""Model (de)serialization: a realistic Contact payload round-trips; NewContact serializes
cleanly to camelCase with no None keys.
"""

from __future__ import annotations

from getresponse.models import CampaignReference, Contact, ContactOrigin, NewContact


def test_contact_deserializes_with_enum_and_camelcase_aliases() -> None:
    payload = {
        "contactId": "abc123",
        "name": "Jane Doe",
        "origin": "api",
        "createdOn": "2024-01-01T00:00:00+00:00",
        "campaign": {"campaignId": "c1", "name": "My Campaign"},
        "email": "jane@example.com",
        "href": "https://api.getresponse.com/v3/contacts/abc123",
    }

    contact = Contact.model_validate(payload)

    assert contact.contact_id == "abc123"
    assert contact.email == "jane@example.com"
    assert contact.origin == ContactOrigin.Api
    assert contact.campaign is not None
    assert contact.campaign.campaign_id == "c1"


def test_new_contact_serializes_to_camelcase_without_none_keys() -> None:
    new_contact = NewContact(
        contact_id="",
        href="",
        email="jane@example.com",
        campaign=CampaignReference(campaign_id="c1"),
        name="Jane Doe",
    )

    dumped = new_contact.model_dump(mode="json", by_alias=True, exclude_none=True)

    assert dumped["email"] == "jane@example.com"
    assert dumped["campaign"]["campaignId"] == "c1"
    assert dumped["contactId"] == ""
    assert "contact_id" not in dumped
    assert all(value is not None for value in dumped.values())
'''

_TEST_PAGINATION = '''"""`GetResponseClient.paginate` walks full pages and stops on a short/empty one."""

from __future__ import annotations

import httpx

from getresponse import GetResponseClient


async def test_paginate_walks_full_pages_then_stops_on_short_page() -> None:
    def contact(i: int) -> dict[str, str]:
        return {"contactId": f"id{i}", "email": f"{i}@example.com", "href": "h"}

    pages = [
        [contact(i) for i in range(50)],
        [contact(i) for i in range(50, 100)],
        [contact(100)],
    ]
    calls = {"count": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        page = int(request.url.params["page"])
        calls["count"] += 1
        return httpx.Response(200, json=pages[page - 1])

    async with GetResponseClient(api_key="k", transport=httpx.MockTransport(handler)) as c:
        seen = [item async for item in c.paginate(c.contacts.get_contact_list, per_page=50)]

    assert len(seen) == 101
    assert calls["count"] == 3
'''

_TEST_ERRORS = '''"""Non-2xx responses raise `GetResponseApiError` with `ErrorResponse` fields populated."""

from __future__ import annotations

import httpx
import pytest

from getresponse import GetResponseApiError, GetResponseClient


async def test_error_response_maps_to_typed_exception() -> None:
    body = {
        "httpStatus": 400,
        "code": 1010,
        "codeDescription": "Invalid value",
        "message": "Email is invalid",
        "moreInfo": "https://apidocs.getresponse.com/errors/1010",
        "context": {"field": "email"},
        "uuid": "abc-123",
    }

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(400, json=body)

    async with GetResponseClient(api_key="k", transport=httpx.MockTransport(handler)) as c:
        with pytest.raises(GetResponseApiError) as exc_info:
            await c.contacts.get_contact_list()

    err = exc_info.value
    assert err.status_code == 400
    assert err.code == 1010
    assert err.message == "Email is invalid"
    assert err.context == {"field": "email"}
    assert err.uuid == "abc-123"
'''

_TEST_RATELIMIT = '''"""Opt-in rate limiter: disabled by default, proactive throttling, and 429 handling."""

from __future__ import annotations

import asyncio

import httpx
import pytest

from getresponse import GetResponseClient, RateLimitError, RateLimitOptions


async def test_disabled_by_default_passes_through_untouched() -> None:
    calls = {"count": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["count"] += 1
        return httpx.Response(200, json=[])

    async with GetResponseClient(api_key="k", transport=httpx.MockTransport(handler)) as c:
        result = await c.contacts.get_contact_list()

    assert result == []
    assert calls["count"] == 1


async def test_reactive_retry_on_429_then_success() -> None:
    calls = {"count": 0}
    sleeps: list[float] = []

    async def fake_sleep(seconds: float) -> None:
        sleeps.append(seconds)

    def handler(request: httpx.Request) -> httpx.Response:
        calls["count"] += 1
        if calls["count"] == 1:
            return httpx.Response(
                429, headers={"X-RateLimit-Reset": "1 seconds"}, json={"httpStatus": 429}
            )
        return httpx.Response(200, json=[])

    options = RateLimitOptions(sleep=fake_sleep)
    async with GetResponseClient(
        api_key="k", transport=httpx.MockTransport(handler), rate_limit=options
    ) as c:
        result = await c.contacts.get_contact_list()

    assert result == []
    assert calls["count"] == 2
    assert sleeps == [1.0]


async def test_cap_then_raise_when_reset_exceeds_max_wait() -> None:
    sleeps: list[float] = []

    async def fake_sleep(seconds: float) -> None:
        sleeps.append(seconds)

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            429, headers={"X-RateLimit-Reset": "9999 seconds"}, json={"httpStatus": 429}
        )

    options = RateLimitOptions(sleep=fake_sleep, max_wait=5.0)
    async with GetResponseClient(
        api_key="k", transport=httpx.MockTransport(handler), rate_limit=options
    ) as c:
        with pytest.raises(RateLimitError) as exc_info:
            await c.contacts.get_contact_list()

    assert exc_info.value.reset_seconds == 9999.0
    assert sleeps == []  # never actually slept for the huge reset


async def test_proactive_concurrency_never_exceeds_max_concurrency() -> None:
    in_flight = {"current": 0, "max": 0}

    async def handler(request: httpx.Request) -> httpx.Response:
        in_flight["current"] += 1
        in_flight["max"] = max(in_flight["max"], in_flight["current"])
        await asyncio.sleep(0.01)
        in_flight["current"] -= 1
        return httpx.Response(200, json=[])

    options = RateLimitOptions(
        max_concurrency=3, requests_per_second=1000, requests_per_window=100000
    )
    async with GetResponseClient(
        api_key="k", transport=httpx.MockTransport(handler), rate_limit=options
    ) as c:
        await asyncio.gather(*(c.contacts.get_contact_list() for _ in range(10)))

    assert in_flight["max"] <= 3


async def test_proactive_rate_pacing_with_fake_clock() -> None:
    class FakeClock:
        def __init__(self) -> None:
            self.now = 0.0

        def __call__(self) -> float:
            return self.now

    clock = FakeClock()
    sleeps: list[float] = []

    async def fake_sleep(seconds: float) -> None:
        sleeps.append(seconds)
        clock.now += seconds

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=[])

    options = RateLimitOptions(
        requests_per_second=2,
        requests_per_window=1000,
        sleep=fake_sleep,
        clock=clock,
    )
    async with GetResponseClient(
        api_key="k", transport=httpx.MockTransport(handler), rate_limit=options
    ) as c:
        for _ in range(4):
            await c.contacts.get_contact_list()

    # capacity starts full (2 tokens): the 3rd and 4th calls each wait ~0.5s for a refill.
    assert len(sleeps) == 2
    assert all(abs(s - 0.5) < 1e-9 for s in sleeps)
'''


# -- orchestration --------------------------------------------------------------------


def _write_once(path: Path, content: str) -> None:
    """Write `content` to `path` only if it doesn't already exist.

    Used for every hand-maintained (scaffold-once) file: written on first generation,
    then left alone on every later regeneration so hand edits survive.
    """
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def emit(api: Api, out_dir: str = "get-response-py") -> None:
    """Render `get-response-py` from `api` and clean it up with ruff.

    Two buckets: `models.py`, `resources/`, and `_resource_groups.py` are spec-derived and
    fully wiped + rewritten every run. Everything else (project/build files, the
    hand-written core runtime, `client.py`, tests) is hand-maintained -- scaffolded once via
    `_write_once` on first generation, then left untouched.
    """
    root = Path(out_dir)
    pkg = root / "getresponse"
    resources_dir = pkg / "resources"
    tests_dir = root / "tests"

    if resources_dir.exists():
        shutil.rmtree(resources_dir)
    for d in (pkg, resources_dir, tests_dir):
        d.mkdir(parents=True, exist_ok=True)

    _write_once(root / "pyproject.toml", _PYPROJECT_TOML)
    _write_once(root / "README.md", _README_MD)

    _write_once(pkg / "__init__.py", _INIT_PY)
    _write_once(pkg / "py.typed", "")
    _write_once(pkg / "_ratelimit.py", _RATELIMIT_PY)
    _write_once(pkg / "_core.py", _CORE_PY)

    (pkg / "models.py").write_text(_render_models_py(api), encoding="utf-8")

    tags = sorted({op.tag for op in api.operations})
    by_tag: dict[str, list[Operation]] = {tag: [] for tag in tags}
    for op in api.operations:
        by_tag[op.tag].append(op)

    (resources_dir / "__init__.py").write_text(_render_resources_init(tags), encoding="utf-8")
    for tag in tags:
        module = _render_resource_module(tag, by_tag[tag])
        (resources_dir / f"{_tag_snake(tag)}.py").write_text(module, encoding="utf-8")

    (pkg / "_resource_groups.py").write_text(_render_resource_groups_py(tags), encoding="utf-8")

    _write_once(pkg / "client.py", _CLIENT_PY)

    _write_once(tests_dir / "conftest.py", _TEST_CONFTEST)
    _write_once(tests_dir / "test_auth.py", _TEST_AUTH)
    _write_once(tests_dir / "test_query_building.py", _TEST_QUERY_BUILDING)
    _write_once(tests_dir / "test_models.py", _TEST_MODELS)
    _write_once(tests_dir / "test_pagination.py", _TEST_PAGINATION)
    _write_once(tests_dir / "test_errors.py", _TEST_ERRORS)
    _write_once(tests_dir / "test_ratelimit.py", _TEST_RATELIMIT)

    print(
        f"wrote {len(tags)} resource modules, models.py, _resource_groups.py "
        f"(scaffold files left untouched if already present) -> {root}"
    )

    subprocess.run([sys.executable, "-m", "ruff", "format", str(root)], check=True)
    subprocess.run(
        [sys.executable, "-m", "ruff", "check", "--fix", str(root)], check=True
    )
