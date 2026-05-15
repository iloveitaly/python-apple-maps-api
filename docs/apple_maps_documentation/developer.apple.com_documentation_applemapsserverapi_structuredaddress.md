---
url: "https://developer.apple.com/documentation/applemapsserverapi/structuredaddress"
title: "StructuredAddress | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/structuredaddress#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- StructuredAddress

Object

# StructuredAddress

An object that describes the detailed address components of a place.

Apple Maps Server API 1.2+

```
object StructuredAddress
```

## [Properties](https://developer.apple.com/documentation/applemapsserverapi/structuredaddress\#properties)

`administrativeArea`

`string`

The state or province of the place.

`administrativeAreaCode`

`string`

The short code for the state or area.

`areasOfInterest`

`[string]`

Common names of the area in which the place resides.

`dependentLocalities`

`[string]`

Common names for the local area or neighborhood of the place.

`fullThoroughfare`

`string`

A combination of thoroughfare and subthoroughfare.

`locality`

`string`

The city of the place.

`postCode`

`string`

The postal code of the place.

`subLocality`

`string`

The name of the area within the locality.

`subThoroughfare`

`string`

The number on the street at the place.

`thoroughfare`

`string`

The street name at the place.

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/structuredaddress\#see-also)

### [Getting common object information](https://developer.apple.com/documentation/applemapsserverapi/structuredaddress\#Getting-common-object-information)

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

[`object SearchResponse`](https://developer.apple.com/documentation/applemapsserverapi/searchresponse)

An object that contains the search region and an array of place descriptions that a search returns.

Current page is StructuredAddress