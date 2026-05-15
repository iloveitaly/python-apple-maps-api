---
url: "https://developer.apple.com/documentation/applemapsserverapi/etaresponse/eta"
title: "EtaResponse.Eta | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/etaresponse/eta#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- [EtaResponse](https://developer.apple.com/documentation/applemapsserverapi/etaresponse)
- EtaResponse.Eta

Object

# EtaResponse.Eta

An object that contains details about an estimated time of arrival (ETA).

Apple Maps Server API 1.2+

```
object EtaResponse.Eta
```

## [Properties](https://developer.apple.com/documentation/applemapsserverapi/etaresponse/eta\#properties)

`destination`

`Location`

The destination as a [`Location`](https://developer.apple.com/documentation/applemapsserverapi/location).

`distanceMeters`

`integer`

The distance in meters to the destination.

`expectedTravelTimeSeconds`

`integer`

The estimated travel time in seconds, including delays due to traffic.

`staticTravelTimeSeconds`

`integer`

The expected travel time, in seconds, without traffic.

`transportType`

`string`

A string that represents the mode of transportation for this ETA, which is one of:

Possible Values: `Automobile, Transit, Walking, Cycling`

Current page is EtaResponse.Eta