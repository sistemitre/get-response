// <scaffolded-once>
// Generated once by codegen/emit_csharp.py; this file is now hand-maintained and safe to
// edit -- regenerating never overwrites it.
// </scaffolded-once>
#nullable enable

using System;
using System.Linq;
using System.Net;
using System.Threading.Tasks;
using System.Web;

using GetResponse.Api;
using GetResponse.Api.Internal;
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

    [Fact]
    public async Task GetContactList_Formats_Datetime_Query_Params_As_GetResponse_Date_Format()
    {
        // GetResponse expects Y-m-d\TH:i:sO (PHP format): no sub-second precision, and the UTC
        // offset without a colon (+0000, not the "O" round-trip format's +00:00).
        var handler = new StubHttpMessageHandler();
        handler.Enqueue(HttpStatusCode.OK, "[]");
        using var client = new GetResponseClient("key", new GetResponseClientOptions { HttpMessageHandler = handler });

        await client.Contacts.GetContactListAsync(
            queryCreatedOnFrom: new DateTimeOffset(2024, 1, 15, 10, 30, 0, 123, TimeSpan.Zero),
            queryCreatedOnTo: new DateTimeOffset(2024, 1, 16, 10, 30, 0, TimeSpan.FromMinutes(330)));

        var request = Assert.Single(handler.Requests);
        var query = HttpUtility.UrlDecode(request.RequestUri!.Query);
        Assert.Contains("query[createdOn][from]=2024-01-15T10:30:00+0000", query);
        Assert.Contains("query[createdOn][to]=2024-01-16T10:30:00+0530", query);
    }

    [Fact]
    public void FormatQueryDate_Matches_GetResponse_Date_Format()
    {
        Assert.Equal(
            "2024-01-15T10:30:00+0000",
            ApiHttp.FormatQueryDate(new DateTimeOffset(2024, 1, 15, 10, 30, 0, 123, TimeSpan.Zero)));
        Assert.Equal(
            "2024-01-16T10:30:00+0530",
            ApiHttp.FormatQueryDate(new DateTimeOffset(2024, 1, 16, 10, 30, 0, TimeSpan.FromMinutes(330))));
    }
}
