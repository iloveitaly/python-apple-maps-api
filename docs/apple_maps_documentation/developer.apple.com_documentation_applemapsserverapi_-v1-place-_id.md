---
url: "https://developer.apple.com/documentation/applemapsserverapi/-v1-place-:id"
title: "Search for a place using an identifier | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-:id#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- Search for a place using an identifier

Web Service Endpoint

# Search for a place using an identifier

Obtain a Place object for a given Place ID.

Apple Maps Server API 1.2+

## [URL](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-:id\#url)

```
GET https://maps-api.apple.com/v1/place/:id
```

## [Path Parameters](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-:id\#path-parameters)

`id`

`string`

(Required)

A single Place ID.

## [Query Parameters](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-:id\#query-parameters)

`lang`

`Lang`

The language code for the response.

Default: `en-US`

## [Response Codes](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-:id\#response-codes)

` 200 OK`

`Place`

`OK`

A [`Place`](https://developer.apple.com/documentation/applemapsserverapi/place) result.

Content-Type: application/json

` 400 Bad Request`

`ErrorResponse`

`Bad Request`

An [`ErrorResponse`](https://developer.apple.com/documentation/applemapsserverapi/errorresponse) object that contains an error message and an array of strings that contain additional details about the error.

Content-Type: application/json

` 401 Unauthorized`

`ErrorResponse`

`Unauthorized`

An [`ErrorResponse`](https://developer.apple.com/documentation/applemapsserverapi/errorresponse) object that contains an error message that indicates the Maps access token is missing or invalid, and an array of strings that contains additional details about the error.

Content-Type: application/json

` 500 Internal Server Error`

`ErrorResponse`

`Internal Server Error`

An [`ErrorResponse`](https://developer.apple.com/documentation/applemapsserverapi/errorresponse) object that contains a server error message and an array of strings that describe additional details about the error.

Content-Type: application/json

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-:id\#see-also)

### [Searching](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-:id\#Searching)

[`type AddressCategory`](https://developer.apple.com/documentation/applemapsserverapi/addresscategory)

Search categories related to political geographical boundaries.

[`type SearchACResultType`](https://developer.apple.com/documentation/applemapsserverapi/searchacresulttype)

An enumerated string that indicates the result type for the search request.

[`type SearchResultType`](https://developer.apple.com/documentation/applemapsserverapi/searchresulttype)

An enumerated string that indicates the result type for the search autocomplete request.

[`object AlternateIdsResponse`](https://developer.apple.com/documentation/applemapsserverapi/alternateidsresponse)

A list of alternate Place IDs and associated errors.

[`object AlternateIdsResponse.AlternateIds`](https://developer.apple.com/documentation/applemapsserverapi/alternateidsresponse/alternateids)

Contains a list of alternate Place IDs for a given Place ID.

[`object PlacesResponse`](https://developer.apple.com/documentation/applemapsserverapi/placesresponse)

A list of Place IDs and errors.

[`object PlacesResponse.PlaceLookupError`](https://developer.apple.com/documentation/applemapsserverapi/placesresponse/placelookuperror)

An error associated with a lookup call.

[`Search for places that match specific criteria`](https://developer.apple.com/documentation/applemapsserverapi/-v1-search)

Find places by name or by specific search criteria.

[`Search for places that meet specific criteria to autocomplete a place search`](https://developer.apple.com/documentation/applemapsserverapi/-v1-searchautocomplete)

Find results that you can use to autocomplete searches.

[`Search for places using mulitple identifiers`](https://developer.apple.com/documentation/applemapsserverapi/-v1-place)

Obtain a set of Place objects for a given set of Place IDs.

[`Obtain a list of alternate place identifiers`](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-alternateids)

Get a list of alternate Place IDs given one or more Place IDs.

Current page is Search for a place using an identifier