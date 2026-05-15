---
url: "https://developer.apple.com/documentation/applemapsserverapi/autocompleteresult"
title: "AutocompleteResult | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/autocompleteresult#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- AutocompleteResult

Object

# AutocompleteResult

An object that contains information you can use to suggest addresses and further refine search results.

Apple Maps Server API 1.2+

```
object AutocompleteResult
```

## [Properties](https://developer.apple.com/documentation/applemapsserverapi/autocompleteresult\#properties)

`completionUrl`

`string`

The relative URI to the `search` endpoint to use to fetch more details pertaining to the result. If available, the framework encodes opaque data about the autocomplete result in the completion URL’s `metadata` parameter.

If clients need to fetch the search result in a certain language, they’re responsible for specifying the `lang` parameter in the request.

`displayLines`

`[string]`

A JSON string array to use to create a long form of display text for the completion result.

`location`

`Location`

A [`Location`](https://developer.apple.com/documentation/applemapsserverapi/location) object that specifies the location of the result in terms of its latitude and longitude.

`structuredAddress`

`StructuredAddress`

A [`StructuredAddress`](https://developer.apple.com/documentation/applemapsserverapi/structuredaddress) object that describes the detailed address components of a place.

## [Discussion](https://developer.apple.com/documentation/applemapsserverapi/autocompleteresult\#Discussion)

If available, the service encodes opaque data about the autocomplete result in the completion URL’s `metadata` parameter. If you need to fetch the search result in a certain language, you need to specify it in the `lang` parameter in the request.

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/autocompleteresult\#see-also)

### [Getting common object information](https://developer.apple.com/documentation/applemapsserverapi/autocompleteresult\#Getting-common-object-information)

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

[`object StructuredAddress`](https://developer.apple.com/documentation/applemapsserverapi/structuredaddress)

An object that describes the detailed address components of a place.

Current page is AutocompleteResult