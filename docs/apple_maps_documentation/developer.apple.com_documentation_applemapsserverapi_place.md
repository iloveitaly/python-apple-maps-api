---
url: "https://developer.apple.com/documentation/applemapsserverapi/place"
title: "Place | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/place#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- Place

Object

# Place

An object that describes a place in terms of a variety of spatial, administrative, and qualitative properties.

Apple Maps Server API 1.2+

```
object Place
```

## [Properties](https://developer.apple.com/documentation/applemapsserverapi/place\#properties)

`country`

`string`

The country or region of the place.

`countryCode`

`string`

The 2-letter country code of the place.

`displayMapRegion`

`MapRegion`

The geographic region associated with the place.

This is a rectangular region on a map expressed as south-west and north-east points. Specifically south latitude, west longitude, north latitude, and east longitude.

`formattedAddressLines`

`[string]`

The address of the place, formatted using its conventions of its country or region.

`name`

`string`

A place name that you can use for display purposes.

`coordinate`

`Location`

The latitude and longitude of this place.

`structuredAddress`

`StructuredAddress`

A [`StructuredAddress`](https://developer.apple.com/documentation/applemapsserverapi/structuredaddress) object that describes details of the place’s address.

`alternateIds`

`[string]`

A list of alternate Place IDs for the `id`.

`id`

`string`

An opaque string that identifies a place.

## [Relationships](https://developer.apple.com/documentation/applemapsserverapi/place\#relationships)

### [Inherited By](https://developer.apple.com/documentation/applemapsserverapi/place\#inherited-by)

- [`SearchResponse.Place`](https://developer.apple.com/documentation/applemapsserverapi/searchresponse/place)

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/place\#see-also)

### [Getting common object information](https://developer.apple.com/documentation/applemapsserverapi/place\#Getting-common-object-information)

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

Current page is Place