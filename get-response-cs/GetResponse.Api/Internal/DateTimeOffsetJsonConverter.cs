// <scaffolded-once>
// Generated once by codegen/emit_csharp.py; this file is now hand-maintained and safe to
// edit -- regenerating never overwrites it.
// </scaffolded-once>
#nullable enable

using System;
using System.Globalization;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace GetResponse.Api.Internal;

/// <summary>
/// Reads the date-time shapes the live API actually sends -- notably a colon-less offset
/// (<c>2026-11-16T10:20:10+0000</c>), which System.Text.Json rejects by default -- plus
/// <c>+00:00</c>, <c>Z</c> and bare dates (taken as UTC midnight). Writing is unchanged
/// (ISO 8601 round-trip). Garbage still throws <see cref="JsonException"/>.
/// </summary>
internal sealed class DateTimeOffsetJsonConverter : JsonConverter<DateTimeOffset>
{
    public override DateTimeOffset Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        if (reader.TokenType != JsonTokenType.String)
        {
            throw new JsonException($"Expected a date-time string, got {reader.TokenType}.");
        }

        return Parse(reader.GetString()!);
    }

    public override void Write(Utf8JsonWriter writer, DateTimeOffset value, JsonSerializerOptions options) =>
        writer.WriteStringValue(value);

    internal static DateTimeOffset Parse(string text)
    {
        // Insert the missing colon in a trailing +HHMM / -HHMM offset.
        var normalized = text.Length >= 5
            && (text[^5] == '+' || text[^5] == '-')
            && char.IsAsciiDigit(text[^4]) && char.IsAsciiDigit(text[^3])
            && char.IsAsciiDigit(text[^2]) && char.IsAsciiDigit(text[^1])
            && text.Contains('T')
                ? text[..^2] + ":" + text[^2..]
                : text;

        if (DateTimeOffset.TryParse(normalized, CultureInfo.InvariantCulture, DateTimeStyles.AssumeUniversal, out var value))
        {
            return value;
        }

        throw new JsonException($"'{text}' is not a date-time the GetResponse API sends.");
    }
}

/// <summary>
/// Nullable counterpart of <see cref="DateTimeOffsetJsonConverter"/>: the API sometimes sends
/// <c>""</c> instead of omitting an optional date, which reads as <c>null</c>.
/// </summary>
internal sealed class NullableDateTimeOffsetJsonConverter : JsonConverter<DateTimeOffset?>
{
    public override bool HandleNull => true;

    public override DateTimeOffset? Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        if (reader.TokenType == JsonTokenType.Null)
        {
            return null;
        }

        if (reader.TokenType != JsonTokenType.String)
        {
            throw new JsonException($"Expected a date-time string, got {reader.TokenType}.");
        }

        var text = reader.GetString();
        return string.IsNullOrWhiteSpace(text) ? null : DateTimeOffsetJsonConverter.Parse(text);
    }

    public override void Write(Utf8JsonWriter writer, DateTimeOffset? value, JsonSerializerOptions options)
    {
        if (value is { } v)
        {
            writer.WriteStringValue(v);
        }
        else
        {
            writer.WriteNullValue();
        }
    }
}
