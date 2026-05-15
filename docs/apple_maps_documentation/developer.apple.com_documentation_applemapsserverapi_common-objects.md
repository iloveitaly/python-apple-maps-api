---
url: "https://developer.apple.com/documentation/applemapsserverapi/common-objects"
title: "Common objects | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/common-objects#app-main)

Collection

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- Common objects

API Collection

# Common objects

Understand the common JSON objects that API responses contain.

## [Topics](https://developer.apple.com/documentation/applemapsserverapi/common-objects\#topics)

### [Getting an access token](https://developer.apple.com/documentation/applemapsserverapi/common-objects\#Getting-an-access-token)

[`object TokenResponse`](https://developer.apple.com/documentation/applemapsserverapi/tokenresponse)

An object that contains an access token and an expiration time in seconds.

### [Getting common object information](https://developer.apple.com/documentation/applemapsserverapi/common-objects\#Getting-common-object-information)

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

[`object StructuredAddress`](https://developer.apple.com/documentation/applemapsserverapi/structuredaddress)

An object that describes the detailed address components of a place.

### [Getting common type information](https://developer.apple.com/documentation/applemapsserverapi/common-objects\#Getting-common-type-information)

[`type CountryCode`](https://developer.apple.com/documentation/applemapsserverapi/countrycode)

A string that represents a two-letter country code.

[`type DirectionsAvoid`](https://developer.apple.com/documentation/applemapsserverapi/directionsavoid)

A list of the features you can request to avoid when calculating directions.

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

### [Handling errors](https://developer.apple.com/documentation/applemapsserverapi/common-objects\#Handling-errors)

[`object ErrorResponse`](https://developer.apple.com/documentation/applemapsserverapi/errorresponse)

Information about an error that occurs while processing a request.

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/common-objects\#see-also)

### [Essentials](https://developer.apple.com/documentation/applemapsserverapi/common-objects\#Essentials)

[Creating and using tokens with Maps Server API](https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api)

Sign JSON Web Tokens to use Maps Server API and debug common signing errors.

[Creating a Maps identifier and a private key](https://developer.apple.com/documentation/applemapsserverapi/creating-a-maps-identifier-and-a-private-key)

Create a Maps identifier and a private key before generating tokens for MapKit JS.

[`Generate a Maps token`](https://developer.apple.com/documentation/applemapsserverapi/-v1-token)

Returns a JWT maps access token that you use to call the service API.

[Debugging an Invalid token](https://developer.apple.com/documentation/applemapsserverapi/debugging-an-invalid-token)

Inspect the JavaScript console logs, the token, and events to determine why a token is invalid.

[Integrating the Apple Maps Server API into Java server applications](https://developer.apple.com/documentation/applemapsserverapi/integrating-the-apple-maps-server-api-into-java-server-applications)

Streamline your app’s API by moving georelated searches from inside your app to your server.

Current page is Common objects