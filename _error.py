"""PytSite Google Maps Plugin Errors
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Error(Exception):
    pass


class GoogleApiKeyNotDefined(Error):
    def __str__(self) -> str:
        return "Registry key 'google_maps.api_key' is not defined or it is empty"


class DistanceCalculationError(Error):
    def __init__(self, google_status: str):
        self._status = google_status

    def __str__(self) -> str:
        return 'Calculation status from Google:'.format(self._status)


class GoogleApiRequestError(Error):
    def __init__(self, request_url: str, request_args: dict, error_content: str):
        super().__init__()

        self._request_url = request_url
        self._request_args = request_args
        self._error_content = error_content

    def __str__(self) -> str:
        return 'Error while requesting Google API {}, {}: {}' \
            .format(self._request_url, self._request_args, self._error_content)


class GoogleApiZeroResults(GoogleApiRequestError):
    pass


class GoogleApiOverQueryLimit(GoogleApiRequestError):
    pass


class GoogleApiRequestDenied(GoogleApiRequestError):
    pass


class GoogleApiInvalidRequest(GoogleApiRequestError):
    pass


class GoogleApiUnknownError(GoogleApiRequestError):
    pass
