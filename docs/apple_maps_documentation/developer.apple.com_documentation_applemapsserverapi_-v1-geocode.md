---
url: "https://developer.apple.com/documentation/applemapsserverapi/-v1-geocode"
title: "Geocode an address | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/-v1-geocode#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- Geocode an address

Web Service Endpoint

# Geocode an address

Returns the latitude and longitude of the address you specify.

Apple Maps Server API 1.2+

## [URL](https://developer.apple.com/documentation/applemapsserverapi/-v1-geocode\#url)

```
GET https://maps-api.apple.com/v1/geocode
```

## [Query Parameters](https://developer.apple.com/documentation/applemapsserverapi/-v1-geocode\#query-parameters)

`q`

`string`

(Required)

The address to geocode. For example: `q=1 Apple Park, Cupertino, CA`

`limitToCountries`

`[string]`

A comma-separated list of two-letter ISO 3166-1 codes to limit the results to. For example: `limitToCountries=US,CA`.

If you specify two or more countries, the results reflect the best available results for some or all of the countries rather than everything related to the query for those countries.

`lang`

`Lang`

The language the server should use when returning the response, specified using a BCP 47 language code. For example, for English use `lang=en-US`.

Default: `en-US`

`searchLocation`

`SearchLocation`

A location defined by the application as a hint. Specify the location as a comma-separated string containing the latitude and longitude. For example, `searchLocation=37.78,-122.42`.

`searchRegion`

`SearchRegion`

A region the app defines as a hint. Specify the region specified as a comma-separated string that describes the region in the form north-latitude, east-longitude, south-latitude, west-longitude. For example, `searchRegion=38,-122.1,37.5,-122.5`.

`userLocation`

`UserLocation`

The location of the user, specified as a comma-separated string that contains the latitude and longitude. For example: `userLocation=37.78,-122.42`.

Certain APIs, such as Searching, may opt to use the `userLocation`, if specified, as a fallback for the `searchLocation`.

## [Response Codes](https://developer.apple.com/documentation/applemapsserverapi/-v1-geocode\#response-codes)

` 200 OK`

`PlaceResults`

`OK`

An array of [`Place`](https://developer.apple.com/documentation/applemapsserverapi/place) objects.

Content-Type: application/json

` 400 Bad Request`

`ErrorResponse`

`Bad Request`

An [`ErrorResponse`](https://developer.apple.com/documentation/applemapsserverapi/errorresponse) object that contains an error message and an array of strings that contains additional details.

Content-Type: application/json

` 401 Unauthorized`

`ErrorResponse`

`Unauthorized`

An [`ErrorResponse`](https://developer.apple.com/documentation/applemapsserverapi/errorresponse) object that contains an error message that indicates the Maps access token was missing or invalid and an array of strings that contains additional details about the error.

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

## [Discussion](https://developer.apple.com/documentation/applemapsserverapi/-v1-geocode\#Discussion)

### [Example](https://developer.apple.com/documentation/applemapsserverapi/-v1-geocode\#Example)

```
curl -si -H "Authorization: Bearer <maps_access_token>" "https://maps-api.apple.com/v1/geocode?q=Apple%20Park%2C%20Cupertino%2C%20CA"
```

```
{
  "results": [\
    {\
      "coordinate": {\
        "latitude": 37.3301996,\
        "longitude": -122.0106415\
      },\
      "displayMapRegion": {\
        "southLatitude": 37.3257080235794,\
        "westLongitude": -122.01629018770203,\
        "northLatitude": 37.3346911764206,\
        "eastLongitude": -122.00499281229798\
      },\
      "name": "Apple Park Way",\
      "formattedAddressLines": [\
        "Apple Park Way",\
        "Cupertino, CA  95014",\
        "United States"\
      ],\
      "structuredAddress": {\
        "administrativeArea": "California",\
        "administrativeAreaCode": "CA",\
        "locality": "Cupertino",\
        "postCode": "95014",\
        "thoroughfare": "Apple Park Way",\
        "fullThoroughfare": "Apple Park Way",\
        "areasOfInterest": [\
          "Apple Park"\
        ]\
      },\
      "country": "United States",\
      "countryCode": "US"\
    }\
  ]
}
```

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/-v1-geocode\#see-also)

### [Geocoding](https://developer.apple.com/documentation/applemapsserverapi/-v1-geocode\#Geocoding)

[`Reverse geocode a location`](https://developer.apple.com/documentation/applemapsserverapi/-v1-reversegeocode)

Returns an array of addresses present at the coordinates you provide.

Current page is Geocode an address