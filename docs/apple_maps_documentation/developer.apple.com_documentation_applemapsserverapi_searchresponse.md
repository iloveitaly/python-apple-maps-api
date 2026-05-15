---
url: "https://developer.apple.com/documentation/applemapsserverapi/searchresponse"
title: "SearchResponse | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/searchresponse#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- SearchResponse

Object

# SearchResponse

An object that contains the search region and an array of place descriptions that a search returns.

Apple Maps Server API 1.2+

```
object SearchResponse
```

## [Properties](https://developer.apple.com/documentation/applemapsserverapi/searchresponse\#properties)

`displayMapRegion`

`SearchMapRegion`

Represents a rectangular region on a map expressed as south-west and north-east points. More specifically south latitude, west longitude, north latitude and east longitude.

`paginationInfo`

`SearchResponse.PaginationInfo`

`results`

`[SearchResponse.Place]`

An array of [`SearchResponse.Place`](https://developer.apple.com/documentation/applemapsserverapi/searchresponse/place) results.

## [Topics](https://developer.apple.com/documentation/applemapsserverapi/searchresponse\#topics)

### [Place information returned by a search](https://developer.apple.com/documentation/applemapsserverapi/searchresponse\#Place-information-returned-by-a-search)

[`object SearchResponse.Place`](https://developer.apple.com/documentation/applemapsserverapi/searchresponse/place)

A structure returned by a search that describes a place.

[`object SearchResponse.PaginationInfo`](https://developer.apple.com/documentation/applemapsserverapi/searchresponse/paginationinfo-data.dictionary)

An object that returns a page of search responses.

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/searchresponse\#see-also)

### [Getting common object information](https://developer.apple.com/documentation/applemapsserverapi/searchresponse\#Getting-common-object-information)

[`object AutocompleteResult`](https://developer.apple.com/documentation/applemapsserverapi/autocompleteresult)

An object that contains information you can use to suggest addresses and further refine search results.

[`object DirectionsResponse`](https://developer.apple.com/documentation/applemapsserverapi/directionsresponse)

An object that describes the directions from a starting location to a destination in terms routes, steps, and a series of waypoints.

[`object EtaResponse`](https://developer.apple.com/documentation/applemapsserverapi/etaresponse)

An object that contains an array of one or more estimated times of arrival (ETAs).

[`object Location`](https://developer.apple.com/documentation/applemapsserverapi/location)

An object that describes a location in terms of its longitude and latitude.

[`object MapRegion`](https://developer.apple.com/documentation/applemapsserverapi/mapregion)

An object that describes a map region in terms of its upper-right and lower-left corners as a pair of geographic points.

[`object Place`](https://developer.apple.com/documentation/applemapsserverapi/place)

An object that describes a place in terms of a variety of spatial, administrative, and qualitative properties.

[`object PlaceResults`](https://developer.apple.com/documentation/applemapsserverapi/placeresults)

An object that contains an array of places.

[`object SearchAutocompleteResponse`](https://developer.apple.com/documentation/applemapsserverapi/searchautocompleteresponse)

An array of autocomplete results.

[`object SearchMapRegion`](https://developer.apple.com/documentation/applemapsserverapi/searchmapregion)

An object that describes an area to search in terms of its upper-right and lower-left corners as a pair of geographic points.

[`object StructuredAddress`](https://developer.apple.com/documentation/applemapsserverapi/structuredaddress)

An object that describes the detailed address components of a place.

Current page is SearchResponse