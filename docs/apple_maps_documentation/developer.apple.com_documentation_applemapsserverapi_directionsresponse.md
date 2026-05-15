---
url: "https://developer.apple.com/documentation/applemapsserverapi/directionsresponse"
title: "DirectionsResponse | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/directionsresponse#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- DirectionsResponse

Object

# DirectionsResponse

An object that describes the directions from a starting location to a destination in terms routes, steps, and a series of waypoints.

Apple Maps Server API 1.2+

```
object DirectionsResponse
```

## [Properties](https://developer.apple.com/documentation/applemapsserverapi/directionsresponse\#properties)

`destination`

`Place`

A [`Place`](https://developer.apple.com/documentation/applemapsserverapi/place) object that describes the destination.

`origin`

`Place`

A [`Place`](https://developer.apple.com/documentation/applemapsserverapi/place) result that describes the origin.

`routes`

`[DirectionsResponse.Route]`

An array of routes. Each route references steps based on indexes into the steps array.

`stepPaths`

`[Location]`

An array of step paths across all steps across all routes. Each step path is a single polyline represented as an array of points. You reference the step paths by index into the array.

`steps`

`[DirectionsResponse.Step]`

An array of all steps across all routes. You reference the route steps by index into this array. Each step in turn references its path based on indexes into the `stepPaths` array.

## [Topics](https://developer.apple.com/documentation/applemapsserverapi/directionsresponse\#topics)

### [Steps and routes](https://developer.apple.com/documentation/applemapsserverapi/directionsresponse\#Steps-and-routes)

[`object DirectionsResponse.Route`](https://developer.apple.com/documentation/applemapsserverapi/directionsresponse/route)

An object that represent the components of a single route.

[`object DirectionsResponse.Step`](https://developer.apple.com/documentation/applemapsserverapi/directionsresponse/step)

An object that represents a step along a route.

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/directionsresponse\#see-also)

### [Getting common object information](https://developer.apple.com/documentation/applemapsserverapi/directionsresponse\#Getting-common-object-information)

[`object AutocompleteResult`](https://developer.apple.com/documentation/applemapsserverapi/autocompleteresult)

An object that contains information you can use to suggest addresses and further refine search results.

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

[`object StructuredAddress`](https://developer.apple.com/documentation/applemapsserverapi/structuredaddress)

An object that describes the detailed address components of a place.

Current page is DirectionsResponse