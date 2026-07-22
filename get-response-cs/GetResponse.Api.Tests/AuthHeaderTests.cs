// <scaffolded-once>
// Generated once by codegen/emit_csharp.py; this file is now hand-maintained and safe to
// edit -- regenerating never overwrites it.
// </scaffolded-once>
#nullable enable

using System.Linq;
using System.Net;
using System.Threading.Tasks;

using GetResponse.Api;

using Xunit;

namespace GetResponse.Api.Tests;

public sealed class AuthHeaderTests
{
    [Fact]
    public async Task ApiKey_Sets_XAuthToken_Header()
    {
        var handler = new StubHttpMessageHandler();
        handler.Enqueue(HttpStatusCode.OK, "[]");
        using var client = new GetResponseClient("secret-key", new GetResponseClientOptions { HttpMessageHandler = handler });

        await client.Contacts.GetContactListAsync();

        var request = Assert.Single(handler.Requests);
        Assert.Equal("api-key secret-key", request.Headers.GetValues("X-Auth-Token").Single());
    }

    [Fact]
    public async Task BearerToken_Sets_Authorization_Header()
    {
        var handler = new StubHttpMessageHandler();
        handler.Enqueue(HttpStatusCode.OK, "[]");
        using var client = GetResponseClient.CreateWithBearerToken(
            "access-token-123",
            new GetResponseClientOptions { HttpMessageHandler = handler });

        await client.Contacts.GetContactListAsync();

        var request = Assert.Single(handler.Requests);
        Assert.Equal("Bearer", request.Headers.Authorization!.Scheme);
        Assert.Equal("access-token-123", request.Headers.Authorization!.Parameter);
    }
}
