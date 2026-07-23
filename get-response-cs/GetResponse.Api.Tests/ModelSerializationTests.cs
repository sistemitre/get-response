// <scaffolded-once>
// Generated once by codegen/emit_csharp.py; this file is now hand-maintained and safe to
// edit -- regenerating never overwrites it.
// </scaffolded-once>
#nullable enable

using System.Text.Json;

using GetResponse.Api;
using GetResponse.Api.Models;

using Xunit;

namespace GetResponse.Api.Tests;

public sealed class ModelSerializationTests
{
    [Fact]
    public void Deserializes_Contact_Json_With_JsonPropertyName_And_Enum()
    {
        const string json =
            "{\"contactId\":\"c1\",\"email\":\"jane@example.com\",\"name\":\"Jane\",\"origin\":\"api\"}";

        var contact = JsonSerializer.Deserialize<ContactListElement>(json, GetResponseClient.JsonOptions);

        Assert.NotNull(contact);
        Assert.Equal("c1", contact!.ContactId);
        Assert.Equal("jane@example.com", contact.Email);
        Assert.Equal("Jane", contact.Name);
        Assert.Equal(ContactListElementOrigin.Api, contact.Origin);
    }

    [Fact]
    public void Deserializes_Empty_String_As_Null_For_Nullable_Enum_Property()
    {
        // GetResponse sometimes returns "" instead of omitting the field for an optional enum
        // with no value (e.g. geolocation.continentCode when the location can't be resolved).
        const string json = "{\"continentCode\":\"\"}";

        var geolocation = JsonSerializer.Deserialize<ContactGeolocation>(json, GetResponseClient.JsonOptions);

        Assert.NotNull(geolocation);
        Assert.Null(geolocation!.ContinentCode);
    }

    [Fact]
    public void Deserializes_Explicit_Null_As_Null_For_Nullable_Enum_Property()
    {
        const string json = "{\"continentCode\":null}";

        var geolocation = JsonSerializer.Deserialize<ContactGeolocation>(json, GetResponseClient.JsonOptions);

        Assert.NotNull(geolocation);
        Assert.Null(geolocation!.ContinentCode);
    }

    [Fact]
    public void Deserializes_Unrecognized_String_As_Unknown_For_NonNullable_Enum_Property()
    {
        // Non-nullable/required enum properties keep the existing forward-compatible fallback:
        // an unrecognized wire value (a brand-new value the live API added, or "") maps to the
        // enum's Unknown member instead of throwing.
        const string json = "{\"conditionType\":\"\",\"operatorType\":\"is\",\"operator\":{}}";

        var condition = JsonSerializer.Deserialize<AutoresponderDayCondition>(json, GetResponseClient.JsonOptions);

        Assert.NotNull(condition);
        Assert.Equal(AutoresponderDayConditionConditionType.Unknown, condition!.ConditionType);
    }

    [Fact]
    public void Serializes_Unset_Nullable_Enum_Property_As_Omitted_Not_Unknown()
    {
        // Guards the write-DTO risk this fix deliberately avoided: UpdateContact.Origin left
        // unset must stay omitted (so the server leaves the field untouched on a partial
        // update), not get serialized as a literal "Unknown" wire value.
        var update = new UpdateContact { Name = "Jane" };

        var json = JsonSerializer.Serialize(update, GetResponseClient.JsonOptions);
        using var doc = JsonDocument.Parse(json);

        Assert.False(doc.RootElement.TryGetProperty("origin", out _));
    }

    [Fact]
    public void Serializes_CreateBody_As_CamelCase_With_Nulls_Omitted()
    {
        var shop = new NewShop { Name = "My Shop", Locale = "en", Currency = "USD" };

        var json = JsonSerializer.Serialize(shop, GetResponseClient.JsonOptions);
        using var doc = JsonDocument.Parse(json);
        var root = doc.RootElement;

        Assert.Equal("My Shop", root.GetProperty("name").GetString());
        Assert.Equal("en", root.GetProperty("locale").GetString());
        Assert.Equal("USD", root.GetProperty("currency").GetString());
        Assert.False(root.TryGetProperty("shopId", out _));
        Assert.False(root.TryGetProperty("href", out _));
        Assert.False(root.TryGetProperty("createdOn", out _));
        Assert.False(root.TryGetProperty("updatedOn", out _));
    }
}
