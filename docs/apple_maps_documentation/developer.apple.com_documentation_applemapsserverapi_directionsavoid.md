---
url: "https://developer.apple.com/documentation/applemapsserverapi/directionsavoid"
title: "DirectionsAvoid | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/directionsavoid#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- DirectionsAvoid

Type

# DirectionsAvoid

A list of the features you can request to avoid when calculating directions.

Apple Maps Server API 1.2+

```
string DirectionsAvoid
```

## [Possible Values](https://developer.apple.com/documentation/applemapsserverapi/directionsavoid\#possibleValues)

`Tolls`

## [Possible Values](https://developer.apple.com/documentation/applemapsserverapi/directionsavoid\#Possible-Values)

Tolls

When you set `avoid=Tolls`, routes without tolls are higher up in the list of returned routes. Note that even when you set `avoid=Tolls`, the routes the server returns may contain tolls (if no reasonable toll-free routes exist). Ensure you check the value of `routes[i].hasTolls` in the response to verify toll assumptions.

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/directionsavoid\#see-also)

### [Getting common type information](https://developer.apple.com/documentation/applemapsserverapi/directionsavoid\#Getting-common-type-information)

[`type CountryCode`](https://developer.apple.com/documentation/applemapsserverapi/countrycode)

A string that represents a two-letter country code.

[`type Lang`](https://developer.apple.com/documentation/applemapsserverapi/lang)

A string that represents a standard tag for identifying languages.

[`type PoiCategory`](https://developer.apple.com/documentation/applemapsserverapi/poicategory)

A string that describes a specific point of interest (POI) category.

[`type SearchLocation`](https://developer.apple.com/documentation/applemapsserverapi/searchlocation)

A string that describes a geographic location in the form of longitude and latitude.

[`type SearchRegion`](https://developer.apple.com/documentation/applemapsserverapi/searchregion)

A string that describes a region to search in terms of its upper-right and lower-left corners as a pair of geographic points.

[`type UserLocation`](https://developer.apple.com/documentation/applemapsserverapi/userlocation)

A string that describes the user’s location in terms of longitude and latitude.

Current page is DirectionsAvoid