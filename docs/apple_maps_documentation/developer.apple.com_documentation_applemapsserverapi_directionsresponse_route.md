---
url: "https://developer.apple.com/documentation/applemapsserverapi/directionsresponse/route"
title: "DirectionsResponse.Route | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/directionsresponse/route#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- [DirectionsResponse](https://developer.apple.com/documentation/applemapsserverapi/directionsresponse)
- DirectionsResponse.Route

Object

# DirectionsResponse.Route

An object that represent the components of a single route.

Apple Maps Server API 1.2+

```
object DirectionsResponse.Route
```

## [Properties](https://developer.apple.com/documentation/applemapsserverapi/directionsresponse/route\#properties)

`distanceMeters`

`integer`

Total distance that the route covers, in meters.

`durationSeconds`

`integer`

The estimated time to traverse this route in seconds. If you’ve specified a `departureDate` or `arrivalDate`, then the estimated time includes traffic conditions assuming user departs or arrives at that time. If you set neither `departureDate` or `arrivalDate`, then estimated time represents current traffic conditions assuming user departs “now” from the point of origin.

`hasTolls`

`boolean`

When `true`, this route has tolls; if `false`, this route has no tolls. If the value isn’t defined (“undefined”), the route may or may not have tolls.

`name`

`string`

The route name that you can use for display purposes.

`stepIndexes`

`[integer]`

An array of integer values that you can use to determine the number steps along this route. Each value in the array corresponds to an index into the `steps` array.

`transportType`

`string`

A string that represents the mode of transportation the service used to estimate the arrival time. Same as the input query param `transportType` or `Automobile` if the input query didn’t specify a transportation type.

Possible Values: `Automobile, Walking, Cycling`

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/directionsresponse/route\#see-also)

### [Steps and routes](https://developer.apple.com/documentation/applemapsserverapi/directionsresponse/route\#Steps-and-routes)

[`object DirectionsResponse.Step`](https://developer.apple.com/documentation/applemapsserverapi/directionsresponse/step)

An object that represents a step along a route.

Current page is DirectionsResponse.Route