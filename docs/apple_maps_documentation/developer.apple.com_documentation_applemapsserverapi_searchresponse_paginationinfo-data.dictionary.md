---
url: "https://developer.apple.com/documentation/applemapsserverapi/searchresponse/paginationinfo-data.dictionary"
title: "SearchResponse.PaginationInfo | Apple Developer Documentation"
---

[Skip Navigation](https://developer.apple.com/documentation/applemapsserverapi/searchresponse/paginationinfo-data.dictionary#app-main)

- [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi)
- [SearchResponse](https://developer.apple.com/documentation/applemapsserverapi/searchresponse)
- SearchResponse.PaginationInfo

Object

# SearchResponse.PaginationInfo

An object that returns a page of search responses.

Apple Maps Server API 1.2+

```
object SearchResponse.PaginationInfo
```

## [Properties](https://developer.apple.com/documentation/applemapsserverapi/searchresponse/paginationinfo-data.dictionary\#properties)

`nextPageToken`

`string`

An opaque string that the server uses to fetch the next page of search responses.

`prevPageToken`

`string`

An opaque string that the server uses to fetch the previous page of search responses.

`totalPageCount`

`number`

The total number of pages for the request.

`totalResults`

`number`

The total number of results for the request.

## [See Also](https://developer.apple.com/documentation/applemapsserverapi/searchresponse/paginationinfo-data.dictionary\#see-also)

### [Place information returned by a search](https://developer.apple.com/documentation/applemapsserverapi/searchresponse/paginationinfo-data.dictionary\#Place-information-returned-by-a-search)

[`object SearchResponse.Place`](https://developer.apple.com/documentation/applemapsserverapi/searchresponse/place)

A structure returned by a search that describes a place.

Current page is SearchResponse.PaginationInfo