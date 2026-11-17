#nullable enable

using System;
using System.Collections.Generic;
using System.Net;
using System.Text.Json;
using System.Threading.Tasks;

using GetResponse.Api;
using GetResponse.Api.Models;

using Xunit;

namespace GetResponse.Api.Tests;

/// <summary>
/// The live API sends date-times with a colon-less offset (<c>2026-11-16T10:20:10+0000</c>), which
/// System.Text.Json rejects by default. These tests pin down that every shape the API actually
/// emits deserializes, through both the shared options and a real resource call.
/// </summary>
public sealed class DateDeserializationTests
{
    public static IEnumerable<object[]> ApiDateShapes() =>
    [
        ["\"2026-11-16T10:20:10+0000\"", new DateTimeOffset(2026, 11, 16, 10, 20, 10, TimeSpan.Zero)],
        ["\"2026-11-16T12:20:10+0200\"", new DateTimeOffset(2026, 11, 16, 12, 20, 10, TimeSpan.FromHours(2))],
        ["\"2026-11-16T05:20:10-0500\"", new DateTimeOffset(2026, 11, 16, 5, 20, 10, TimeSpan.FromHours(-5))],
        ["\"2026-11-16T10:20:10+00:00\"", new DateTimeOffset(2026, 11, 16, 10, 20, 10, TimeSpan.Zero)],
        ["\"2026-11-16T10:20:10Z\"", new DateTimeOffset(2026, 11, 16, 10, 20, 10, TimeSpan.Zero)],
        ["\"2026-11-16T10:20:10.123+0000\"", new DateTimeOffset(2026, 11, 16, 10, 20, 10, 123, TimeSpan.Zero)],
        ["\"2026-11-16\"", new DateTimeOffset(2026, 11, 16, 0, 0, 0, TimeSpan.Zero)],
    ];

    [Theory]
    [MemberData(nameof(ApiDateShapes))]
    public void Every_Api_Date_Shape_Deserializes(string json, DateTimeOffset expected)
    {
        Assert.Equal(expected, JsonSerializer.Deserialize<DateTimeOffset>(json, GetResponseClient.JsonOptions));
        Assert.Equal(expected, JsonSerializer.Deserialize<DateTimeOffset?>(json, GetResponseClient.JsonOptions));
    }

    [Theory]
    [InlineData("null")]
    [InlineData("\"\"")]
    public void Null_Or_Empty_String_Is_Null_For_Optional_Dates(string json)
    {
        Assert.Null(JsonSerializer.Deserialize<DateTimeOffset?>(json, GetResponseClient.JsonOptions));
    }

    [Fact]
    public void Garbage_Still_Fails_Loudly()
    {
        Assert.Throws<JsonException>(() => JsonSerializer.Deserialize<DateTimeOffset>("\"not a date\"", GetResponseClient.JsonOptions));
    }

    [Fact]
    public void Writing_Keeps_The_Iso_8601_Round_Trip_Format()
    {
        var value = new DateTimeOffset(2026, 11, 16, 10, 20, 10, TimeSpan.FromHours(1));

        Assert.Equal("\"2026-11-16T10:20:10+01:00\"", JsonSerializer.Serialize(value, GetResponseClient.JsonOptions));
        Assert.Equal("\"2026-11-16T10:20:10+01:00\"", JsonSerializer.Serialize((DateTimeOffset?)value, GetResponseClient.JsonOptions));
    }

    [Fact]
    public async Task Contact_With_Live_Api_Dates_Deserializes_Through_A_Resource_Call()
    {
        // Shape captured from GET /contacts/{id} on the live API.
        const string contactJson =
            "{\"contactId\":\"pV3r\",\"href\":\"https://api.getresponse.com/v3/contacts/pV3r\","
            + "\"email\":\"jane@example.com\",\"createdOn\":\"2026-11-16T10:20:10+0000\","
            + "\"changedOn\":\"2026-11-17T08:00:00+0000\",\"campaign\":{\"campaignId\":\"uEmrP\"},"
            + "\"tags\":[],\"customFieldValues\":[]}";
        var handler = new StubHttpMessageHandler();
        handler.Enqueue(HttpStatusCode.OK, contactJson);
        using var client = new GetResponseClient("key", new GetResponseClientOptions { HttpMessageHandler = handler });

        var contact = await client.Contacts.GetContactByIdAsync("pV3r");

        Assert.Equal(new DateTimeOffset(2026, 11, 16, 10, 20, 10, TimeSpan.Zero), contact.CreatedOn);
        Assert.Equal(new DateTimeOffset(2026, 11, 17, 8, 0, 0, TimeSpan.Zero), contact.ChangedOn);
    }

    [Fact]
    public async Task Activities_With_Live_Api_Dates_Deserialize()
    {
        const string activitiesJson =
            "[{\"activity\":\"click\",\"subject\":\"News\",\"createdOn\":\"2026-11-05T09:12:30+0000\","
            + "\"previewUrl\":null,\"resource\":{\"resourceId\":\"N1\",\"resourceType\":\"newsletters\"},"
            + "\"clickTrack\":{\"id\":\"ct1\",\"name\":\"site\",\"url\":\"https://example.com\"}}]";
        var handler = new StubHttpMessageHandler();
        handler.Enqueue(HttpStatusCode.OK, activitiesJson);
        using var client = new GetResponseClient("key", new GetResponseClientOptions { HttpMessageHandler = handler });

        var activities = await client.Contacts.GetActivitiesAsync("pV3r");

        Assert.Equal(new DateTimeOffset(2026, 11, 5, 9, 12, 30, TimeSpan.Zero), Assert.Single(activities).CreatedOn);
    }
}
