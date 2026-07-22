// <scaffolded-once>
// Generated once by codegen/emit_csharp.py; this file is now hand-maintained and safe to
// edit -- regenerating never overwrites it.
// </scaffolded-once>
#nullable enable

using System;
using System.Collections.Generic;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace GetResponse.Api.Internal;

/// <summary>
/// Caches each enum member's <see cref="EnumMemberAttribute"/> wire string in both directions.
/// Backs <see cref="EnumMemberJsonConverter{T}"/> and the query-string building generated
/// resource-client methods do for enum-typed filters, so the wire mapping lives exactly once,
/// on the enum's own members, regardless of who needs it.
/// </summary>
internal static class EnumWireValues<T>
    where T : struct, Enum
{
    public static readonly IReadOnlyDictionary<string, T> FromWireValue;
    public static readonly IReadOnlyDictionary<T, string> ToWireValue;

    static EnumWireValues()
    {
        var fromWire = new Dictionary<string, T>(StringComparer.Ordinal);
        var toWire = new Dictionary<T, string>();
        foreach (var field in typeof(T).GetFields(BindingFlags.Public | BindingFlags.Static))
        {
            var value = (T)field.GetValue(null)!;
            var wire = field.GetCustomAttribute<EnumMemberAttribute>()?.Value ?? field.Name;
            fromWire[wire] = value;
            toWire[value] = wire;
        }
        FromWireValue = fromWire;
        ToWireValue = toWire;
    }
}

/// <summary>Creates an <see cref="EnumMemberJsonConverter{T}"/> for every enum type.</summary>
internal sealed class EnumMemberJsonConverterFactory : JsonConverterFactory
{
    public override bool CanConvert(Type typeToConvert) => typeToConvert.IsEnum;

    public override JsonConverter CreateConverter(Type typeToConvert, JsonSerializerOptions options)
    {
        var converterType = typeof(EnumMemberJsonConverter<>).MakeGenericType(typeToConvert);
        return (JsonConverter)Activator.CreateInstance(converterType)!;
    }
}

/// <summary>
/// (De)serializes an enum using each member's <see cref="EnumMemberAttribute"/> wire string
/// rather than its C# name. An unrecognized wire value maps to the enum's <c>Unknown</c> member
/// instead of failing, so a new server-side value never breaks deserialization.
/// </summary>
internal sealed class EnumMemberJsonConverter<T> : JsonConverter<T>
    where T : struct, Enum
{
    public override T Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        var wire = reader.GetString();
        if (wire is not null && EnumWireValues<T>.FromWireValue.TryGetValue(wire, out var value))
        {
            return value;
        }
        return default;
    }

    public override void Write(Utf8JsonWriter writer, T value, JsonSerializerOptions options)
    {
        writer.WriteStringValue(EnumWireValues<T>.ToWireValue.TryGetValue(value, out var wire) ? wire : value.ToString());
    }
}
