// <scaffolded-once>
// Generated once by codegen/emit_csharp.py; this file is now hand-maintained and safe to
// edit -- regenerating never overwrites it.
// </scaffolded-once>
#nullable enable

using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text.Json;
using System.Text.Json.Serialization;

using GetResponse.Api.Internal;

namespace GetResponse.Api;

/// <summary>
/// Root client for the GetResponse v3 API. Authenticate with an API key (the primary
/// constructor) or an OAuth2 bearer token (<see cref="CreateWithBearerToken"/>), then call
/// operations through the resource-group properties, e.g. <see cref="Contacts"/>.
/// </summary>
public sealed partial class GetResponseClient : IDisposable
{
    /// <summary>The default production API base URL.</summary>
    public const string BaseUrlDefault = "https://api.getresponse.com/v3";

    /// <summary>The GetResponse MAX (US) base URL.</summary>
    public const string BaseUrlMaxUs = "https://api3.getresponse360.com/v3";

    /// <summary>The GetResponse MAX (PL) base URL.</summary>
    public const string BaseUrlMaxPl = "https://api3.getresponse360.pl/v3";

    /// <summary>
    /// The <see cref="JsonSerializerOptions"/> shared by every model and resource client:
    /// property names come from <c>[JsonPropertyName]</c>, enums (de)serialize via their
    /// <c>[EnumMember]</c> wire value, and null properties are omitted when writing.
    /// </summary>
    public static readonly JsonSerializerOptions JsonOptions = CreateJsonOptions();

    private readonly HttpClient _httpClient;
    private readonly bool _ownsHttpClient;
    private readonly RequestRateLimiter? _rateLimiter;

    /// <summary>Creates a client authenticated with an API key, sent as the <c>X-Auth-Token: api-key &lt;key&gt;</c> header.</summary>
    public GetResponseClient(string apiKey, GetResponseClientOptions? options = null)
    {
        ArgumentException.ThrowIfNullOrEmpty(apiKey);
        options ??= new GetResponseClientOptions();
        _httpClient = BuildHttpClient(options);
        _ownsHttpClient = true;
        _httpClient.DefaultRequestHeaders.Add("X-Auth-Token", $"api-key {apiKey}");
        _rateLimiter = BuildRateLimiter(options);
        var pipeline = new ApiHttp(_httpClient, options.BaseUrl, JsonOptions, _rateLimiter);
        InitializeResourceGroups(pipeline);
    }

    /// <summary>Wraps an already-configured <see cref="HttpClient"/> (e.g. one with a custom handler pipeline, or a stub transport in tests). The caller retains ownership and is responsible for disposing it.</summary>
    public GetResponseClient(HttpClient httpClient)
    {
        ArgumentNullException.ThrowIfNull(httpClient);
        _httpClient = httpClient;
        _ownsHttpClient = false;
        var baseUrl = httpClient.BaseAddress?.ToString() ?? BaseUrlDefault;
        var pipeline = new ApiHttp(_httpClient, baseUrl, JsonOptions);
        InitializeResourceGroups(pipeline);
    }

    private GetResponseClient(GetResponseClientOptions options)
    {
        _httpClient = BuildHttpClient(options);
        _ownsHttpClient = true;
        _rateLimiter = BuildRateLimiter(options);
        var pipeline = new ApiHttp(_httpClient, options.BaseUrl, JsonOptions, _rateLimiter);
        InitializeResourceGroups(pipeline);
    }

    /// <summary>Creates a client authenticated with an OAuth2 bearer access token, sent as the <c>Authorization: Bearer &lt;token&gt;</c> header.</summary>
    public static GetResponseClient CreateWithBearerToken(string accessToken, GetResponseClientOptions? options = null)
    {
        ArgumentException.ThrowIfNullOrEmpty(accessToken);
        var client = new GetResponseClient(options ?? new GetResponseClientOptions());
        client._httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", accessToken);
        return client;
    }

    /// <summary>Disposes the underlying <see cref="HttpClient"/> (if this client created and owns it) and the rate limiter (if configured).</summary>
    public void Dispose()
    {
        if (_ownsHttpClient)
        {
            _httpClient.Dispose();
        }
        _rateLimiter?.Dispose();
    }

    private static HttpClient BuildHttpClient(GetResponseClientOptions options)
    {
        var handler = options.HttpMessageHandler ?? new HttpClientHandler();
        return new HttpClient(handler) { Timeout = options.Timeout };
    }

    /// <summary>Builds the opt-in rate limiter from <see cref="GetResponseClientOptions.RateLimit"/>, or <c>null</c> when unset or disabled.</summary>
    private static RequestRateLimiter? BuildRateLimiter(GetResponseClientOptions options) =>
        options.RateLimit is { Enabled: true } rateLimit ? new RequestRateLimiter(rateLimit) : null;

    private static JsonSerializerOptions CreateJsonOptions()
    {
        var options = new JsonSerializerOptions
        {
            DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull,
        };
        options.Converters.Add(new EnumMemberJsonConverterFactory());
        return options;
    }
}
