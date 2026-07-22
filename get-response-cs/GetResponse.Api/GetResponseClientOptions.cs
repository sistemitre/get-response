// <scaffolded-once>
// Generated once by codegen/emit_csharp.py; this file is now hand-maintained and safe to
// edit -- regenerating never overwrites it.
// </scaffolded-once>
#nullable enable

using System;
using System.Net.Http;

namespace GetResponse.Api;

/// <summary>Configuration for <see cref="GetResponseClient"/>: target environment, timeout, and (for tests) a custom transport.</summary>
public sealed class GetResponseClientOptions
{
    /// <summary>The API base URL. Defaults to <see cref="GetResponseClient.BaseUrlDefault"/>.</summary>
    public string BaseUrl { get; init; } = GetResponseClient.BaseUrlDefault;

    /// <summary>The HTTP request timeout. Defaults to 100 seconds.</summary>
    public TimeSpan Timeout { get; init; } = TimeSpan.FromSeconds(100);

    /// <summary>
    /// A custom transport, e.g. a stub <see cref="HttpMessageHandler"/> in tests. When set, it is
    /// disposed together with the <see cref="HttpClient"/> the client builds around it.
    /// </summary>
    public HttpMessageHandler? HttpMessageHandler { get; init; }

    /// <summary>
    /// Opt-in client-side rate limiting (concurrency, per-second/per-window request budgets, and
    /// 429 retry). Disabled unless assigned.
    /// </summary>
    public RateLimitOptions? RateLimit { get; init; }
}
