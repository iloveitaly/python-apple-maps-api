---
url: "https://developer.apple.com/documentation/applemapsserverapi/placesresponse"
title: "PlacesResponse | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/placesresponse#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- PlacesResponse

Object

# PlacesResponse

A list of Place IDs and errors.

Apple Maps Server API 1.2+

```
object PlacesResponse
```

## [Properties](https://developer.apple.com/documentation/applemapsserverapi/placesresponse\#properties)

`errors`

`[PlacesResponse.PlaceLookupError]`

A list of [`PlacesResponse.PlaceLookupError`](https://developer.apple.com/documentation/applemapsserverapi/placesresponse/placelookuperror) results.

`results`

`[Place]`

A list of [`Place`](https://developer.apple.com/documentation/applemapsserverapi/place) results.

## [Topics](https://developer.apple.com/documentation/applemapsserverapi/placesresponse\#topics)

### [Objects](https://developer.apple.com/documentation/applemapsserverapi/placesresponse\#Objects)

[`object PlacesResponse.PlaceLookupError`](https://developer.apple.com/documentation/applemapsserverapi/placesresponse/placelookuperror)

An error associated with a lookup call.

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/placesresponse\#see-also)

### [Searching](https://developer.apple.com/documentation/applemapsserverapi/placesresponse\#Searching)

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

[`Obtain a list of alternate place identifiers`](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-alternateids)

Get a list of alternate Place IDs given one or more Place IDs.

Current page is PlacesResponse