---
url: "https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api"
title: "Creating and using tokens with Maps Server API | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- Creating and using tokens with Maps Server API

Article

# Creating and using tokens with Maps Server API

Sign JSON Web Tokens to use Maps Server API and debug common signing errors.

## [Overview](https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api\#overview)

Maps Server API uses a Maps token to authenticate map initializations and other API requests, such as requests to retrieve directions or execute a search. To use a Maps token with Maps Server API you must have an Apple Developer account and obtain a Maps ID and a private key as described in [Creating a Maps identifier and a private key](https://developer.apple.com/documentation/applemapsserverapi/creating-a-maps-identifier-and-a-private-key).

After getting or creating a token, confirm the success of the token authorization by using the token to access the API; check the status code that the functions return to verify the calls were successful.

### [Create a Token to Use Maps Server API](https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api\#Create-a-Token-to-Use-Maps-Server-API)

Maps Server API requires a Maps token to initialize MapKit. A Maps token has two sections, a header and a payload. The header describes the token and the cryptographic operations applied to the payload. The payload contains a set of cryptographically signed claims.

Construct a token with these required fields in the header:

- `alg` — The algorithm you use to encrypt the token. Use the `ES256` algorithm to encrypt your token.

- `kid` — A 10-character key identifier that provides the ID of the private key that you obtain from your Apple Developer account.

- `typ` — A type parameter that you set to `"JWT"`.


In the payload section of the token, include the following claims:

- `iss` — The issuer of the token. This is a 10-character Team ID obtained from your Apple Developer account.

- `iat` — The Issued At registered claim key. The value of this claim indicates the token creation time, in terms of the number of seconds since UNIX Epoch, in UTC.

- `exp` — The Expiration Time registered claim key. The value of this claim indicates when the token expires, in terms of the number of seconds since UNIX Epoch, in UTC.


To locate your Team ID, sign in to your [Apple Developer account](https://developer.apple.com/account), and click Membership in the sidebar. Your Team ID appears in the Membership information section under the team name. Generate your token by signing it with your private key.

When decoded, a token for use with Maps Server API has the following format:

```
{
    "alg": "ES256",
    "kid": "ABC123DEFG",
    "typ": "JWT"
}
{
    "iss": "DEF123GHIJ",
    "iat": 1437179036,
    "exp": 1493298100,
    "origin": "*.example.com"
}
```

To learn more about Maps tokens, see the [JSON Web Token (JWT) specification](https://tools.ietf.org/html/rfc7519). You can find a collection of libraries for generating signed tokens at [JWT.io](https://jwt.io/).

For next steps, go to [`Generate a Maps token`](https://developer.apple.com/documentation/applemapsserverapi/-v1-token).

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api\#see-also)

### [Essentials](https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api\#Essentials)

[Creating a Maps identifier and a private key](https://developer.apple.com/documentation/applemapsserverapi/creating-a-maps-identifier-and-a-private-key)

Create a Maps identifier and a private key before generating tokens for MapKit JS.

[`Generate a Maps token`](https://developer.apple.com/documentation/applemapsserverapi/-v1-token)

Returns a JWT maps access token that you use to call the service API.

[Debugging an Invalid token](https://developer.apple.com/documentation/applemapsserverapi/debugging-an-invalid-token)

Inspect the JavaScript console logs, the token, and events to determine why a token is invalid.

[API Reference\\
Common objects](https://developer.apple.com/documentation/applemapsserverapi/common-objects)

Understand the common JSON objects that API responses contain.

[Integrating the Apple Maps Server API into Java server applications](https://developer.apple.com/documentation/applemapsserverapi/integrating-the-apple-maps-server-api-into-java-server-applications)

Streamline your app’s API by moving georelated searches from inside your app to your server.

Current page is Creating and using tokens with Maps Server API