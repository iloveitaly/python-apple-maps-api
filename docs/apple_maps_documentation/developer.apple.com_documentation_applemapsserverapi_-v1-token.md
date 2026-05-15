---
url: "https://developer.apple.com/documentation/applemapsserverapi/-v1-token"
title: "Generate a Maps token | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/-v1-token#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- Generate a Maps token

Web Service Endpoint

# Generate a Maps token

Returns a JWT maps access token that you use to call the service API.

Apple Maps Server API 1.2+

## [URL](https://developer.apple.com/documentation/applemapsserverapi/-v1-token\#url)

```
GET https://maps-api.apple.com/v1/token
```

## [Response Codes](https://developer.apple.com/documentation/applemapsserverapi/-v1-token\#response-codes)

` 200 OK`

`TokenResponse`

`OK`

A response that indicates the authorization request is successful. The dictionary that accompanies the response contains a maps access token and an integer that indicates the time in seconds until the token expires.

Content-Type: application/json

` 401 Unauthorized`

`ErrorResponse`

`Unauthorized`

An error response that indicates the maps token is missing or invalid. The dictionary that accompanies the error may contain additional details about the error.

Content-Type: application/json

` 429`

`ErrorResponse`

``

An [`ErrorResponse`](https://developer.apple.com/documentation/applemapsserverapi/errorresponse) object that indicates the call exceeds the daily service call quota for the authorization token presented. The app should try again later. If your app requires a larger daily quota, submit a [quota increase request form](https://developer.apple.com/contact/request/mapkitjs/).

Content-Type: application/json

` 500 Internal Server Error`

`ErrorResponse`

`Internal Server Error`

An error that indicates the server can’t complete the request. The dictionary that accompanies the error may contain additional details about the error.

Content-Type: application/json

## [Mentioned in](https://developer.apple.com/documentation/applemapsserverapi/-v1-token\#mentions)

[Creating and using tokens with Maps Server API](https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api)

## [Discussion](https://developer.apple.com/documentation/applemapsserverapi/-v1-token\#Discussion)

### [Example](https://developer.apple.com/documentation/applemapsserverapi/-v1-token\#Example)

```
curl -si -H "Authorization: Bearer <maps_auth_token>" "https://maps-api.apple.com/v1/token"
```

```
{
  "accessToken": "<maps_access_token>",
  "expiresInSeconds": 1800
}
```

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/-v1-token\#see-also)

### [Essentials](https://developer.apple.com/documentation/applemapsserverapi/-v1-token\#Essentials)

[Creating and using tokens with Maps Server API](https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api)

Sign JSON Web Tokens to use Maps Server API and debug common signing errors.

[Creating a Maps identifier and a private key](https://developer.apple.com/documentation/applemapsserverapi/creating-a-maps-identifier-and-a-private-key)

Create a Maps identifier and a private key before generating tokens for MapKit JS.

[Debugging an Invalid token](https://developer.apple.com/documentation/applemapsserverapi/debugging-an-invalid-token)

Inspect the JavaScript console logs, the token, and events to determine why a token is invalid.

[API Reference\\
Common objects](https://developer.apple.com/documentation/applemapsserverapi/common-objects)

Understand the common JSON objects that API responses contain.

[Integrating the Apple Maps Server API into Java server applications](https://developer.apple.com/documentation/applemapsserverapi/integrating-the-apple-maps-server-api-into-java-server-applications)

Streamline your app’s API by moving georelated searches from inside your app to your server.

Current page is Generate a Maps token