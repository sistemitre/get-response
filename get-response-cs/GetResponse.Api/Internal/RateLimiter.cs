// <scaffolded-once>
// Generated once by codegen/emit_csharp.py; this file is now hand-maintained and safe to
// edit -- regenerating never overwrites it.
// </scaffolded-once>
#nullable enable

using System;
using System.Globalization;
using System.Linq;
using System.Net.Http;
using System.Threading;
using System.Threading.RateLimiting;
using System.Threading.Tasks;

namespace GetResponse.Api.Internal;

/// <summary>
/// Enforces <see cref="RateLimitOptions"/>: a <see cref="ConcurrencyLimiter"/> plus per-second and
/// per-window <see cref="SlidingWindowRateLimiter"/>s bound outgoing requests, and best-effort
/// adaptive back-off reacts to the API's <c>X-RateLimit-*</c> response headers. One instance is
/// shared by every request <see cref="ApiHttp"/> sends.
/// </summary>
internal sealed class RequestRateLimiter : IDisposable
{
    private readonly RateLimitOptions _options;
    private readonly RateLimiter _concurrency;
    private readonly RateLimiter _perSecond;
    private readonly RateLimiter _perWindow;
    private DateTimeOffset? _blockedUntilUtc;

    public RequestRateLimiter(RateLimitOptions options)
    {
        _options = options;
        _concurrency = new ConcurrencyLimiter(new ConcurrencyLimiterOptions
        {
            PermitLimit = Math.Max(1, options.MaxConcurrency),
            QueueProcessingOrder = QueueProcessingOrder.OldestFirst,
            QueueLimit = int.MaxValue,
        });
        _perSecond = new SlidingWindowRateLimiter(new SlidingWindowRateLimiterOptions
        {
            PermitLimit = EffectiveLimit(options.RequestsPerSecond, options.SafetyMargin),
            Window = TimeSpan.FromSeconds(1),
            SegmentsPerWindow = 10,
            QueueProcessingOrder = QueueProcessingOrder.OldestFirst,
            QueueLimit = int.MaxValue,
        });
        _perWindow = new SlidingWindowRateLimiter(new SlidingWindowRateLimiterOptions
        {
            PermitLimit = EffectiveLimit(options.RequestsPerWindow, options.SafetyMargin),
            Window = TimeSpan.FromSeconds(Math.Max(1, options.WindowSeconds)),
            SegmentsPerWindow = 60,
            QueueProcessingOrder = QueueProcessingOrder.OldestFirst,
            QueueLimit = int.MaxValue,
        });
    }

    /// <summary>Retries allowed after a 429 before <see cref="ApiHttp"/> gives up and throws.</summary>
    public int MaxRetries => _options.MaxRetries;

    /// <summary>Cap, in seconds, on any single wait.</summary>
    public int MaxWaitSeconds => _options.MaxWaitSeconds;

    /// <summary>The injected delay primitive (defaults to <see cref="Task.Delay(TimeSpan, CancellationToken)"/>).</summary>
    public Task DelayAsync(TimeSpan delay, CancellationToken ct) => _options.DelayAsync(delay, ct);

    /// <summary>
    /// Proactively acquires a concurrency slot plus a per-second and per-window permit, after
    /// waiting out any adaptive back-off recorded by <see cref="ObserveResponse"/>. Throws
    /// <see cref="RateLimitException"/> if the combined wait would exceed
    /// <see cref="RateLimitOptions.MaxWaitSeconds"/>.
    /// </summary>
    public async Task<IDisposable> AcquireAsync(CancellationToken ct)
    {
        using var cts = CancellationTokenSource.CreateLinkedTokenSource(ct);
        cts.CancelAfter(TimeSpan.FromSeconds(_options.MaxWaitSeconds));
        try
        {
            await WaitForAdaptiveBackoffAsync(cts.Token).ConfigureAwait(false);

            var concurrency = await _concurrency.AcquireAsync(1, cts.Token).ConfigureAwait(false);
            if (!concurrency.IsAcquired)
            {
                concurrency.Dispose();
                throw CapExceeded();
            }

            var perSecond = await _perSecond.AcquireAsync(1, cts.Token).ConfigureAwait(false);
            if (!perSecond.IsAcquired)
            {
                perSecond.Dispose();
                concurrency.Dispose();
                throw CapExceeded();
            }

            var perWindow = await _perWindow.AcquireAsync(1, cts.Token).ConfigureAwait(false);
            if (!perWindow.IsAcquired)
            {
                perWindow.Dispose();
                perSecond.Dispose();
                concurrency.Dispose();
                throw CapExceeded();
            }

            return new CompositeLease(concurrency, perSecond, perWindow);
        }
        catch (OperationCanceledException) when (!ct.IsCancellationRequested)
        {
            throw CapExceeded();
        }
    }

    /// <summary>Records a zero-remaining response so the next <see cref="AcquireAsync"/> call backs off (best-effort).</summary>
    public void ObserveResponse(HttpResponseMessage response)
    {
        var remaining = TryGetHeaderInt(response, "X-RateLimit-Remaining");
        if (remaining is null || remaining.Value > 0)
        {
            return;
        }
        var resetSeconds = ParseResetHeader(response) ?? _options.WindowSeconds;
        var candidate = DateTimeOffset.UtcNow.AddSeconds(resetSeconds);
        if (_blockedUntilUtc is null || candidate > _blockedUntilUtc.Value)
        {
            _blockedUntilUtc = candidate;
        }
    }

    public void Dispose()
    {
        _concurrency.Dispose();
        _perSecond.Dispose();
        _perWindow.Dispose();
    }

    private async Task WaitForAdaptiveBackoffAsync(CancellationToken ct)
    {
        var until = _blockedUntilUtc;
        if (until is null)
        {
            return;
        }
        _blockedUntilUtc = null;
        var wait = until.Value - DateTimeOffset.UtcNow;
        if (wait > TimeSpan.Zero)
        {
            await _options.DelayAsync(wait, ct).ConfigureAwait(false);
        }
    }

    private RateLimitException CapExceeded() => new(_options.MaxWaitSeconds, _options.MaxWaitSeconds);

    private static int EffectiveLimit(int configured, double safetyMargin) =>
        Math.Max(1, (int)Math.Floor(configured * safetyMargin));

    /// <summary>Parses the leading integer out of an <c>X-RateLimit-Reset: "432 seconds"</c> header, if present.</summary>
    internal static int? ParseResetHeader(HttpResponseMessage response) => TryGetHeaderInt(response, "X-RateLimit-Reset");

    /// <summary>Reads a response header as a leading integer (e.g. <c>"432 seconds"</c> or <c>"17"</c>), if present.</summary>
    internal static int? TryGetHeaderInt(HttpResponseMessage response, string name)
    {
        if (!response.Headers.TryGetValues(name, out var values))
        {
            return null;
        }
        var raw = values.FirstOrDefault();
        if (string.IsNullOrWhiteSpace(raw))
        {
            return null;
        }
        var span = raw.AsSpan().TrimStart();
        var digits = 0;
        while (digits < span.Length && char.IsDigit(span[digits]))
        {
            digits++;
        }
        return digits > 0 && int.TryParse(span[..digits], NumberStyles.None, CultureInfo.InvariantCulture, out var value)
            ? value
            : null;
    }

    /// <summary>Releases the concurrency, per-second, and per-window leases together as one <see cref="AcquireAsync"/> result.</summary>
    private sealed class CompositeLease : IDisposable
    {
        private readonly RateLimitLease _concurrency;
        private readonly RateLimitLease _perSecond;
        private readonly RateLimitLease _perWindow;

        public CompositeLease(RateLimitLease concurrency, RateLimitLease perSecond, RateLimitLease perWindow)
        {
            _concurrency = concurrency;
            _perSecond = perSecond;
            _perWindow = perWindow;
        }

        public void Dispose()
        {
            _concurrency.Dispose();
            _perSecond.Dispose();
            _perWindow.Dispose();
        }
    }
}
