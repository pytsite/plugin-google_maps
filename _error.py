"""PytSite Google Maps Plugin Errors
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class GoogleApiKeyNotDefined(Exception):
    pass


class DistanceCalculationError(Exception):
    pass


class GoogleApiError(Exception):
    def __init__(self, api_url: str, request_args: dict, error_content: str):
        super().__init__()

        self._api_url = api_url
        self._request_args = request_args
        self._error_content = error_content

    def __str__(self) -> str:
        return 'Error while requesting Google API {}, {}: {}' \
            .format(self._api_url, self._request_args, self._error_content)


class GoogleApiZeroResults(GoogleApiError):
    pass


class GoogleApiOverQueryLimit(GoogleApiError):
    pass


class GoogleApiRequestDenied(GoogleApiError):
    pass


class GoogleApiInvalidRequest(GoogleApiError):
    pass


class GoogleApiUnknownError(GoogleApiError):
    pass
