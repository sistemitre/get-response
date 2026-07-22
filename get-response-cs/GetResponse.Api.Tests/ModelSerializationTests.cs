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
