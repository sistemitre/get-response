// <scaffolded-once>
// Generated once by codegen/emit_csharp.py; this file is now hand-maintained and safe to
// edit -- regenerating never overwrites it.
// </scaffolded-once>
#nullable enable

using System.Linq;
using System.Net;
using System.Threading.Tasks;
using System.Web;

using GetResponse.Api;
using GetResponse.Api.Models;

using Xunit;

namespace GetResponse.Api.Tests;

public sealed class QueryBuildingTests
{
    [Fact]
    public async Task GetContactList_Builds_Bracket_Notation_Query_String()
    {
        var handler = new StubHttpMessageHandler();
        handler.Enqueue(HttpStatusCode.OK, "[]");
        using var client = new GetResponseClient("key", new GetResponseClientOptions { HttpMessageHandler = handler });

        await client.Contacts.GetContactListAsync(
            queryEmail: "jane@example.com",
            sortName: SortOrderEnum.Asc,
            page: 2,
            perPage: 50);

        var request = Assert.Single(handler.Requests);
        var query = HttpUtility.UrlDecode(request.RequestUri!.Query);
        Assert.Contains("query[email]=jane@example.com", query);
        Assert.Contains("sort[name]=ASC", query);
        Assert.Contains("page=2", query);
        Assert.Contains("perPage=50", query);
        Assert.DoesNotContain("query[name]", query);
        Assert.DoesNotContain("query[campaignId]", query);
    }
}
