---
url: "https://developer.apple.com/documentation/applemapsserverapi/addresscategory"
title: "AddressCategory | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/addresscategory#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- AddressCategory

Type

# AddressCategory

Search categories related to political geographical boundaries.

Apple Maps Server API 1.2+

```
string AddressCategory
```

## [Possible Values](https://developer.apple.com/documentation/applemapsserverapi/addresscategory\#possibleValues)

`Country`

`AdministrativeArea`

`SubAdministrativeArea`

`Locality`

`SubLocality`

`PostalCode`

## [Possible Values](https://developer.apple.com/documentation/applemapsserverapi/addresscategory\#Possible-Values)

Country

Countries and regions. AdministrativeArea The primary administrative divisions of countries or regions.

SubAdministrativeArea

The secondary administrative divisions of countries or regions.

Locality

Local administrative divisions, postal cities and populated places.

SubLocality

Local administrative sub-divisions, postal city sub-districts, and neighborhoods.

PostalCode

A code assigned to addresses for mail sorting and delivery.

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/addresscategory\#see-also)

### [Searching](https://developer.apple.com/documentation/applemapsserverapi/addresscategory\#Searching)

[`type SearchACResultType`](https://developer.apple.com/documentation/applemapsserverapi/searchacresulttype)

An enumerated string that indicates the result type for the search request.

[`type SearchResultType`](https://developer.apple.com/documentation/applemapsserverapi/searchresulttype)

An enumerated string that indicates the result type for the search autocomplete request.

[`object AlternateIdsResponse`](https://developer.apple.com/documentation/applemapsserverapi/alternateidsresponse)

A list of alternate Place IDs and associated errors.

[`object AlternateIdsResponse.AlternateIds`](https://developer.apple.com/documentation/applemapsserverapi/alternateidsresponse/alternateids)

Contains a list of alternate Place IDs for a given Place ID.

[`object PlacesResponse`](https://developer.apple.com/documentation/applemapsserverapi/placesresponse)

A list of Place IDs and errors.

[`object PlacesResponse.PlaceLookupError`](https://developer.apple.com/documentation/applemapsserverapi/placesresponse/placelookuperror)

An error associated with a lookup call.

[`Search for places that match specific criteria`](https://developer.apple.com/documentation/applemapsserverapi/-v1-search)

Find places by name or by specific search criteria.

[`Search for places that meet specific criteria to autocomplete a place search`](https://developer.apple.com/documentation/applemapsserverapi/-v1-searchautocomplete)

Find results that you can use to autocomplete searches.

[`Search for a place using an identifier`](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-:id)

Obtain a Place object for a given Place ID.

[`Search for places using mulitple identifiers`](https://developer.apple.com/documentation/applemapsserverapi/-v1-place)

Obtain a set of Place objects for a given set of Place IDs.

[`Obtain a list of alternate place identifiers`](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-alternateids)

Get a list of alternate Place IDs given one or more Place IDs.

Current page is AddressCategory