class AppleMapsError(Exception):
    """Base exception for all Apple Maps API errors."""
    pass

class AppleMapsAuthError(AppleMapsError):
    """Raised when authentication fails (e.g., invalid JWT, expired token)."""
    pass

class AppleMapsRequestError(AppleMapsError):
    """Raised when the API returns a client error (4xx besides 429)."""
    def __init__(self, message, status_code=None, response=None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response

class AppleMapsRateLimitError(AppleMapsRequestError):
    """Raised when the API returns a 429 Too Many Requests error."""
    pass

class AppleMapsServerError(AppleMapsError):
    """Raised when the API returns a 5xx server error."""
    def __init__(self, message, status_code=None, response=None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response
