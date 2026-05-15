---
url: "https://developer.apple.com/documentation/applemapsserverapi/-v1-place-alternateids"
title: "Obtain a list of alternate place identifiers | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-alternateids#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- Obtain a list of alternate place identifiers

Web Service Endpoint

# Obtain a list of alternate place identifiers

Get a list of alternate Place IDs given one or more Place IDs.

Apple Maps Server API 1.2+

## [URL](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-alternateids\#url)

```
GET https://maps-api.apple.com/v1/place/alternateIds
```

## [Query Parameters](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-alternateids\#query-parameters)

`ids`

`string`

(Required)

A list of alternate Place IDs.

## [Response Codes](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-alternateids\#response-codes)

` 200 OK`

`AlternateIdsResponse`

`OK`

A list of [`AlternateIdsResponse`](https://developer.apple.com/documentation/applemapsserverapi/alternateidsresponse) results.

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

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-alternateids\#see-also)

### [Searching](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-alternateids\#Searching)

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

[`Search for a place using an identifier`](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-:id)

Obtain a Place object for a given Place ID.

[`Search for places using mulitple identifiers`](https://developer.apple.com/documentation/applemapsserverapi/-v1-place)

Obtain a set of Place objects for a given set of Place IDs.

Current page is Obtain a list of alternate place identifiers