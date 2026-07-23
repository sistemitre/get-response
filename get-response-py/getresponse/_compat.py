"""Hand-maintained compatibility helpers for the generated models/enums. Not regenerated."""

from __future__ import annotations

from enum import Enum


class _UnknownFallbackEnum(str, Enum):
    """Base class for every generated enum.

    GetResponse sometimes sends a wire value this client doesn't recognize -- either
    literally `""` instead of `null` for an optional enum with no value (e.g.
    `geolocation.continentCode` when the location can't be resolved), or a genuinely new
    value the API started returning after this client was generated. Either way, this
    resolves to the enum's own `UNKNOWN` member (defined on every generated enum) instead
    of raising, so a new server-side value never breaks deserialization.
    """

    @classmethod
    def _missing_(cls, value: object) -> _UnknownFallbackEnum:
        return cls.UNKNOWN  # type: ignore[attr-defined]
