---
url: "https://developer.apple.com/documentation/applemapsserverapi/searchacresulttype"
title: "SearchACResultType | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/searchacresulttype#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- SearchACResultType

Type

# SearchACResultType

An enumerated string that indicates the result type for the search request.

Apple Maps Server API 1.2+

```
string SearchACResultType
```

## [Possible Values](https://developer.apple.com/documentation/applemapsserverapi/searchacresulttype\#possibleValues)

`poi`

`address`

`physicalFeature`

`pointOfInterest`

`query`

## [Possible Values](https://developer.apple.com/documentation/applemapsserverapi/searchacresulttype\#Possible-Values)

poi

A point of interest. address An address such as a street address, suburb, city, state, or country.

physicalFeature

A natural physical feature, such as a river, mountain, or delta.

pointOfInterest

A point of interest. query A search query string.

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/searchacresulttype\#see-also)

### [Searching](https://developer.apple.com/documentation/applemapsserverapi/searchacresulttype\#Searching)

[`type AddressCategory`](https://developer.apple.com/documentation/applemapsserverapi/addresscategory)

Search categories related to political geographical boundaries.

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

Current page is SearchACResultType