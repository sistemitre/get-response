// <scaffolded-once>
// Generated once by codegen/emit_csharp.py; this file is now hand-maintained and safe to
// edit -- regenerating never overwrites it.
// </scaffolded-once>
#nullable enable

using System;
using System.Text.Json;

using GetResponse.Api.Models;

namespace GetResponse.Api;

/// <summary>Thrown when the GetResponse API responds with a non-success HTTP status. Carries the parsed <c>ErrorResponse</c> fields when the body could be parsed as one.</summary>
public class GetResponseApiException : Exception
{
    /// <summary>The HTTP status code returned by the API.</summary>
    public int StatusCode { get; }

    /// <summary>The API-specific error code, when the error body was parsed.</summary>
    public int? Code { get; }

    /// <summary>A short description of <see cref="Code"/>, when the error body was parsed.</summary>
    public string? CodeDescription { get; }

    /// <summary>A URL to this error's documentation, when the error body was parsed.</summary>
    public string? MoreInfo { get; }

    /// <summary>Additional structured error context, when the error body was parsed.</summary>
    public JsonElement? Context { get; }

    /// <summary>The error's correlation UUID, when the error body was parsed.</summary>
    public string? Uuid { get; }

    internal GetResponseApiException(int statusCode, ErrorResponse? error, string? rawBody)
        : base(BuildMessage(statusCode, error, rawBody))
    {
        StatusCode = statusCode;
        Code = error?.Code;
        CodeDescription = error?.CodeDescription;
        MoreInfo = error?.MoreInfo;
        Context = error?.Context;
        Uuid = error?.Uuid;
    }

    private static string BuildMessage(int statusCode, ErrorResponse? error, string? rawBody)
    {
        if (error is not null)
        {
            return error.Message;
        }
        return string.IsNullOrWhiteSpace(rawBody)
            ? $"GetResponse API request failed with status {statusCode}."
            : $"GetResponse API request failed with status {statusCode}: {rawBody}";
    }
}
