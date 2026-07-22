// <scaffolded-once>
// Generated once by codegen/emit_csharp.py; this file is now hand-maintained and safe to
// edit -- regenerating never overwrites it.
// </scaffolded-once>
#nullable enable

using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace GetResponse.Api.Tests;

/// <summary>
/// A minimal <see cref="HttpMessageHandler"/> stub: replays a queue of canned responses, a single
/// fixed (sync or async) responder, and records every request it sees, so tests can assert on the
/// request that generated code built without touching the network. Thread-safe, so tests can also
/// fire concurrent requests at it (e.g. to exercise rate-limiter concurrency).
/// </summary>
internal sealed class StubHttpMessageHandler : HttpMessageHandler
{
    private readonly object _gate = new();
    private readonly Queue<HttpResponseMessage> _responses = new();
    private readonly List<HttpRequestMessage> _requests = new();
    private Func<HttpRequestMessage, HttpResponseMessage>? _responder;
    private Func<HttpRequestMessage, CancellationToken, Task<HttpResponseMessage>>? _asyncResponder;

    public IReadOnlyList<HttpRequestMessage> Requests
    {
        get
        {
            lock (_gate)
            {
                return _requests.ToList();
            }
        }
    }

    public void Enqueue(HttpStatusCode status, string? json = null)
    {
        var response = new HttpResponseMessage(status);
        if (json is not null)
        {
            response.Content = new StringContent(json, Encoding.UTF8, "application/json");
        }
        lock (_gate)
        {
            _responses.Enqueue(response);
        }
    }

    /// <summary>Installs a synchronous per-request responder, e.g. one that varies its reply based on <see cref="Requests"/>.Count.</summary>
    public void Respond(Func<HttpRequestMessage, HttpResponseMessage> responder)
    {
        _responder = responder;
    }

    /// <summary>Installs an async per-request responder -- e.g. one that awaits <see cref="Task.Delay(int, CancellationToken)"/> so concurrent requests genuinely overlap.</summary>
    public void RespondAsync(Func<HttpRequestMessage, CancellationToken, Task<HttpResponseMessage>> responder)
    {
        _asyncResponder = responder;
    }

    protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken ct)
    {
        lock (_gate)
        {
            _requests.Add(request);
        }
        if (_asyncResponder is not null)
        {
            return await _asyncResponder(request, ct).ConfigureAwait(false);
        }
        if (_responder is not null)
        {
            return _responder(request);
        }
        lock (_gate)
        {
            if (_responses.Count > 0)
            {
                return _responses.Dequeue();
            }
        }
        return new HttpResponseMessage(HttpStatusCode.OK);
    }
}
