---
url: "https://developer.apple.com/documentation/applemapsserverapi/-v1-etas"
title: "Determine estimated arrival times and distances to one or more destinations | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/-v1-etas#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- Determine estimated arrival times and distances to one or more destinations

Web Service Endpoint

# Determine estimated arrival times and distances to one or more destinations

Returns the estimated time of arrival (ETA) and distance between starting and ending locations.

Apple Maps Server API 1.2+

## [URL](https://developer.apple.com/documentation/applemapsserverapi/-v1-etas\#url)

```
GET https://maps-api.apple.com/v1/etas
```

## [Query Parameters](https://developer.apple.com/documentation/applemapsserverapi/-v1-etas\#query-parameters)

`origin`

`string`

(Required)

The starting point for estimated arrival time requests, specified as a comma-separated string that contains the latitude and longitude. For example, `origin=37.331423,-122.030503`.

`destinations`

`[string]`

(Required)

Destination coordinates represented as pairs of latitude and longitude separated by a vertical bar character (”\|”).

For example, `destinations=37.32556561130194,-121.94635203581443|37.44176585512703,-122.17259315798667`.

The parameter must specify at least one destination coordinate, but no more than 10 destinations. Specify the location as a comma-separated string that contains the latitude and longitude.

`transportType`

`string`

The mode of transportation to use when estimating arrival times.

Default: `Automobile`

Possible Values: `Automobile, Transit, Walking, Cycling`

`departureDate`

`string`

The time of departure to use in an estimated arrival time request, in ISO 8601 format in UTC time.

For example, `departureDate=2020-09-15T16:42:00Z`.

If you don’t specify a departure date, the server uses the current date and time when you make the request.

`arrivalDate`

`string`

The intended time of arrival in ISO 8601 format in UTC time.

## [Response Codes](https://developer.apple.com/documentation/applemapsserverapi/-v1-etas\#response-codes)

` 200 OK`

`EtaResponse`

`OK`

An array of [`EtaResponse`](https://developer.apple.com/documentation/applemapsserverapi/etaresponse) objects that contain distance and time from the origin to each destination.

Content-Type: application/json

` 400 Bad Request`

`ErrorResponse`

`Bad Request`

An [`ErrorResponse`](https://developer.apple.com/documentation/applemapsserverapi/errorresponse) object that contains an error message and an array of strings that contain additional details.

Content-Type: application/json

` 401 Unauthorized`

`ErrorResponse`

`Unauthorized`

An [`ErrorResponse`](https://developer.apple.com/documentation/applemapsserverapi/errorresponse) object that contains an error message that indicates the Maps access token is missing or invalid, and an array of strings that contains additional details about the error.

Content-Type: application/json

` 429`

`ErrorResponse`

``

An [`ErrorResponse`](https://developer.apple.com/documentation/applemapsserverapi/errorresponse) object that indicates the call exceeds the daily service call quota for the authorization token presented. The app should try again later. If your app requires a larger daily quota, submit a [quota increase request form](https://developer.apple.com/contact/request/mapkitjs/).

Content-Type: application/json

` 500 Internal Server Error`

`ErrorResponse`

`Internal Server Error`

An [`ErrorResponse`](https://developer.apple.com/documentation/applemapsserverapi/errorresponse) object that contains a server error message and an array of strings that describe additional details about the error.

Content-Type: application/json

## [Discussion](https://developer.apple.com/documentation/applemapsserverapi/-v1-etas\#Discussion)

### [Example](https://developer.apple.com/documentation/applemapsserverapi/-v1-etas\#Example)

```
curl -si -H "Authorization: Bearer <maps_access_token>" "https://maps-api.apple.com/v1/etas?origin=37.331423,-122.030503&destinations=37.32556561130194,-121.94635203581443|37.44176585512703,-122.17259315798667"
```

```
{
  "etas": [\
    {\
      "destination": {\
        "latitude": 37.32556561130194,\
        "longitude": -121.94635203581443\
      },\
      "transportType": "AUTOMOBILE",\
      "distanceMeters": 9550,\
      "expectedTravelTimeSeconds": 975,\
      "staticTravelTimeSeconds": 540\
    },\
    {\
      "destination": {\
        "latitude": 37.44176585512703,\
        "longitude": -122.17259315798667\
      },\
      "transportType": "AUTOMOBILE",\
      "distanceMeters": 23286,\
      "expectedTravelTimeSeconds": 1336,\
      "staticTravelTimeSeconds": 1039\
    }\
  ]
}
```

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/-v1-etas\#see-also)

### [Directions](https://developer.apple.com/documentation/applemapsserverapi/-v1-etas\#Directions)

[`Search for directions and estimated travel time between locations`](https://developer.apple.com/documentation/applemapsserverapi/-v1-directions)

Find directions by specific criteria.

Current page is Determine estimated arrival times and distances to one or more destinations