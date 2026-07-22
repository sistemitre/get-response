// <scaffolded-once>
// Generated once by codegen/emit_csharp.py; this file is now hand-maintained and safe to
// edit -- regenerating never overwrites it.
// </scaffolded-once>
#nullable enable

using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading;
using System.Threading.Tasks;

using GetResponse.Api.Models;

namespace GetResponse.Api.Internal;

/// <summary>
/// The shared HTTP request pipeline used by every resource client: substitutes path parameters,
/// builds the bracket-notation query string (skipping null values), serializes the JSON or
/// multipart body, dispatches the call -- retrying on HTTP 429 when a
/// <see cref="RequestRateLimiter"/> is configured -- and maps non-success responses to
/// <see cref="GetResponseApiException"/>.
/// </summary>
public sealed class ApiHttp
{
    private readonly HttpClient _httpClient;
    private readonly string _baseUrl;
    private readonly JsonSerializerOptions _json;
    private readonly RequestRateLimiter? _rateLimiter;

    internal ApiHttp(HttpClient httpClient, string baseUrl, JsonSerializerOptions json, RequestRateLimiter? rateLimiter = null)
    {
        _httpClient = httpClient;
        _baseUrl = baseUrl.TrimEnd('/');
        _json = json;
        _rateLimiter = rateLimiter;
    }

    /// <summary>Sends a request and deserializes the JSON response body into <typeparamref name="T"/>, or <c>default</c> for an empty/204 response.</summary>
    public async Task<T?> SendAsync<T>(
        HttpMethod method,
        string pathTemplate,
        IReadOnlyDictionary<string, string?>? pathParams,
        IReadOnlyList<KeyValuePair<string, string?>>? query,
        object? body,
        bool multipart,
        CancellationToken ct)
    {
        using var response = await SendCoreAsync(method, pathTemplate, pathParams, query, body, multipart, ct)
            .ConfigureAwait(false);
        var content = await response.Content.ReadAsStringAsync(ct).ConfigureAwait(false);
        return string.IsNullOrWhiteSpace(content) ? default : JsonSerializer.Deserialize<T>(content, _json);
    }

    /// <summary>Sends a request that returns no response body.</summary>
    public async Task SendAsync(
        HttpMethod method,
        string pathTemplate,
        IReadOnlyDictionary<string, string?>? pathParams,
        IReadOnlyList<KeyValuePair<string, string?>>? query,
        object? body,
        bool multipart,
        CancellationToken ct)
    {
        using var response = await SendCoreAsync(method, pathTemplate, pathParams, query, body, multipart, ct)
            .ConfigureAwait(false);
    }

    private Task<HttpResponseMessage> SendCoreAsync(
        HttpMethod method,
        string pathTemplate,
        IReadOnlyDictionary<string, string?>? pathParams,
        IReadOnlyList<KeyValuePair<string, string?>>? query,
        object? body,
        bool multipart,
        CancellationToken ct)
    {
        var uri = BuildUri(pathTemplate, pathParams, query);
        // No rate limiter configured: identical to the pre-rate-limiting single-shot send, with
        // zero extra allocations or awaits.
        return _rateLimiter is null
            ? SendOnceAsync(method, uri, body, multipart, ct)
            : SendWithRateLimitAsync(_rateLimiter, method, uri, body, multipart, ct);
    }

    private async Task<HttpResponseMessage> SendOnceAsync(
        HttpMethod method, Uri uri, object? body, bool multipart, CancellationToken ct)
    {
        using var request = BuildRequest(method, uri, body, multipart);
        var response = await _httpClient.SendAsync(request, HttpCompletionOption.ResponseContentRead, ct)
            .ConfigureAwait(false);
        if (!response.IsSuccessStatusCode)
        {
            await ThrowApiExceptionAsync(response, ct).ConfigureAwait(false);
        }
        return response;
    }

    /// <summary>Acquires a permit, sends, and -- on HTTP 429 -- delays and retries up to <see cref="RateLimitOptions.MaxRetries"/> times.</summary>
    private async Task<HttpResponseMessage> SendWithRateLimitAsync(
        RequestRateLimiter limiter, HttpMethod method, Uri uri, object? body, bool multipart, CancellationToken ct)
    {
        for (var attempt = 0; ; attempt++)
        {
            using var lease = await limiter.AcquireAsync(ct).ConfigureAwait(false);
            var request = BuildRequest(method, uri, body, multipart);
            HttpResponseMessage response;
            try
            {
                response = await _httpClient.SendAsync(request, HttpCompletionOption.ResponseContentRead, ct)
                    .ConfigureAwait(false);
            }
            finally
            {
                // Multipart content is owned by the caller (its own `using` disposes it once the
                // final attempt returns) and must survive an earlier retry, so detach it before
                // this request disposes its content.
                if (multipart)
                {
                    request.Content = null;
                }
                request.Dispose();
            }

            limiter.ObserveResponse(response);
            if (response.StatusCode != HttpStatusCode.TooManyRequests)
            {
                if (!response.IsSuccessStatusCode)
                {
                    await ThrowApiExceptionAsync(response, ct).ConfigureAwait(false);
                }
                return response;
            }

            var (error, rawBody) = await ReadErrorBodyAsync(response, ct).ConfigureAwait(false);
            var resetSeconds = RequestRateLimiter.ParseResetHeader(response) ?? TryGetContextTimeToReset(error) ?? 0;
            var limitHeader = RequestRateLimiter.TryGetHeaderInt(response, "X-RateLimit-Limit");
            var remainingHeader = RequestRateLimiter.TryGetHeaderInt(response, "X-RateLimit-Remaining");
            response.Dispose();

            if (attempt >= limiter.MaxRetries || resetSeconds > limiter.MaxWaitSeconds)
            {
                throw new RateLimitException(
                    (int)HttpStatusCode.TooManyRequests, error, rawBody, resetSeconds, limitHeader, remainingHeader);
            }

            await limiter.DelayAsync(TimeSpan.FromSeconds(resetSeconds), ct).ConfigureAwait(false);
        }
    }

    private HttpRequestMessage BuildRequest(HttpMethod method, Uri uri, object? body, bool multipart)
    {
        var request = new HttpRequestMessage(method, uri);
        if (multipart)
        {
            if (body is HttpContent content)
            {
                request.Content = content;
            }
        }
        else if (body is not null)
        {
            var payload = JsonSerializer.Serialize(body, body.GetType(), _json);
            request.Content = new StringContent(payload, Encoding.UTF8, "application/json");
        }
        return request;
    }

    private Uri BuildUri(
        string pathTemplate,
        IReadOnlyDictionary<string, string?>? pathParams,
        IReadOnlyList<KeyValuePair<string, string?>>? query)
    {
        var path = pathTemplate;
        if (pathParams is not null)
        {
            foreach (var (key, value) in pathParams)
            {
                path = path.Replace("{" + key + "}", Uri.EscapeDataString(value ?? string.Empty), StringComparison.Ordinal);
            }
        }

        var builder = new StringBuilder(_baseUrl);
        builder.Append(path);

        if (query is not null)
        {
            var first = true;
            foreach (var (key, value) in query)
            {
                if (value is null)
                {
                    continue;
                }
                builder.Append(first ? '?' : '&');
                first = false;
                builder.Append(Uri.EscapeDataString(key)).Append('=').Append(Uri.EscapeDataString(value));
            }
        }

        return new Uri(builder.ToString(), UriKind.Absolute);
    }

    private async Task ThrowApiExceptionAsync(HttpResponseMessage response, CancellationToken ct)
    {
        var (error, rawBody) = await ReadErrorBodyAsync(response, ct).ConfigureAwait(false);
        throw new GetResponseApiException((int)response.StatusCode, error, rawBody);
    }

    private async Task<(ErrorResponse? Error, string RawBody)> ReadErrorBodyAsync(HttpResponseMessage response, CancellationToken ct)
    {
        var rawBody = await response.Content.ReadAsStringAsync(ct).ConfigureAwait(false);
        ErrorResponse? error = null;
        if (!string.IsNullOrWhiteSpace(rawBody))
        {
            try
            {
                error = JsonSerializer.Deserialize<ErrorResponse>(rawBody, _json);
            }
            catch (JsonException)
            {
                // Fall through: an unparsable body still surfaces via the raw-body fallback message.
            }
        }
        return (error, rawBody);
    }

    /// <summary>Falls back to the <c>ErrorResponse.context.timeToReset</c> field when the <c>X-RateLimit-Reset</c> header is missing or unparsable.</summary>
    private static int? TryGetContextTimeToReset(ErrorResponse? error)
    {
        if (error?.Context is not { ValueKind: JsonValueKind.Object } context)
        {
            return null;
        }
        return context.TryGetProperty("timeToReset", out var prop) && prop.TryGetInt32(out var value) ? value : null;
    }
}
