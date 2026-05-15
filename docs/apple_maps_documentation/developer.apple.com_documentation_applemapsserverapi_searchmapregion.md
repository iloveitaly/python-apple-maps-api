---
url: "https://developer.apple.com/documentation/applemapsserverapi/searchmapregion"
title: "SearchMapRegion | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/searchmapregion#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- SearchMapRegion

Object

# SearchMapRegion

An object that describes an area to search in terms of its upper-right and lower-left corners as a pair of geographic points.

Apple Maps Server API 1.2+

```
object SearchMapRegion
```

## [Properties](https://developer.apple.com/documentation/applemapsserverapi/searchmapregion\#properties)

`eastLongitude`

`double`

A double value that describes the east longitude of the map region.

`northLatitude`

`double`

A double value that describes the north latitude of the map region.

`southLatitude`

`double`

A double value that describes the south latitude of the map region.

`westLongitude`

`double`

A double value that describes west longitude of the map region.

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/searchmapregion\#see-also)

### [Getting common object information](https://developer.apple.com/documentation/applemapsserverapi/searchmapregion\#Getting-common-object-information)

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

[`object SearchResponse`](https://developer.apple.com/documentation/applemapsserverapi/searchresponse)

An object that contains the search region and an array of place descriptions that a search returns.

[`object StructuredAddress`](https://developer.apple.com/documentation/applemapsserverapi/structuredaddress)

An object that describes the detailed address components of a place.

Current page is SearchMapRegion