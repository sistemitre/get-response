// <scaffolded-once>
// Generated once by codegen/emit_csharp.py; this file is now hand-maintained and safe to
// edit -- regenerating never overwrites it.
// </scaffolded-once>
#nullable enable

using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

using GetResponse.Api;

using Xunit;

namespace GetResponse.Api.Tests;

public sealed class PaginationTests
{
    [Fact]
    public async Task PaginateAsync_Walks_Pages_Until_A_Short_Page()
    {
        var pages = new List<IReadOnlyList<int>>
        {
            Enumerable.Range(1, 3).ToList(),
            Enumerable.Range(4, 3).ToList(),
            Enumerable.Range(7, 1).ToList(),
        };
        var calls = 0;

        Task<IReadOnlyList<int>> FetchPage(int page, int perPage, CancellationToken ct)
        {
            calls++;
            return Task.FromResult(pages[page - 1]);
        }

        var results = new List<int>();
        await foreach (var item in Pagination.PaginateAsync(FetchPage, perPage: 3))
        {
            results.Add(item);
        }

        Assert.Equal(Enumerable.Range(1, 7), results);
        Assert.Equal(3, calls);
    }
}
