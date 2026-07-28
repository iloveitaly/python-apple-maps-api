# apple_maps_api.exceptions

## Exceptions

| [`AppleMapsError`](#apple_maps_api.exceptions.AppleMapsError)                   | Base exception for all Apple Maps API errors.                        |
|---------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [`AppleMapsAuthError`](#apple_maps_api.exceptions.AppleMapsAuthError)           | Raised when authentication fails (e.g., invalid JWT, expired token). |
| [`AppleMapsRequestError`](#apple_maps_api.exceptions.AppleMapsRequestError)     | Raised when the API returns a client error (4xx besides 429).        |
| [`AppleMapsRateLimitError`](#apple_maps_api.exceptions.AppleMapsRateLimitError) | Raised when the API returns a 429 Too Many Requests error.           |
| [`AppleMapsServerError`](#apple_maps_api.exceptions.AppleMapsServerError)       | Raised when the API returns a 5xx server error.                      |

## Module Contents

### *exception* apple_maps_api.exceptions.AppleMapsError

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception)

Base exception for all Apple Maps API errors.

### *exception* apple_maps_api.exceptions.AppleMapsAuthError

Bases: [`AppleMapsError`](#apple_maps_api.exceptions.AppleMapsError)

Raised when authentication fails (e.g., invalid JWT, expired token).

### *exception* apple_maps_api.exceptions.AppleMapsRequestError(message, status_code=None, response=None)

Bases: [`AppleMapsError`](#apple_maps_api.exceptions.AppleMapsError)

Raised when the API returns a client error (4xx besides 429).

#### status_code *= None*

#### response *= None*

### *exception* apple_maps_api.exceptions.AppleMapsRateLimitError(message, status_code=None, response=None)

Bases: [`AppleMapsRequestError`](#apple_maps_api.exceptions.AppleMapsRequestError)

Raised when the API returns a 429 Too Many Requests error.

### *exception* apple_maps_api.exceptions.AppleMapsServerError(message, status_code=None, response=None)

Bases: [`AppleMapsError`](#apple_maps_api.exceptions.AppleMapsError)

Raised when the API returns a 5xx server error.

#### status_code *= None*

#### response *= None*
