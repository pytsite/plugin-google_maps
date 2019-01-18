"""PytSite Google Maps Plugin Helper Functions
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import requests as _requests
from pytsite import reg as _reg, lang as _lang
from . import _error


def get_google_api_key() -> str:
    """Get configured Google Maps API key.
    """
    api_key = _reg.get('google_maps.api_key')
    if not api_key:
        raise _error.GoogleApiKeyNotDefined()

    return api_key


def google_api_request(api: str, args: dict, language: str = None):
    if api not in ('geocode', 'timezone', 'distancematrix'):
        raise _error.Error('Invalid or unsupported Google API: {}'.format(api))

    args.update({
        'key': get_google_api_key(),
        'language': language or _lang.get_current(),
    })

    url = 'https://maps.googleapis.com/maps/api/{}/json'.format(api)
    resp = _requests.get(url, args)

    if not resp.ok:
        raise _error.GoogleApiRequestError(url, args, resp.content.decode('utf-8'))

    resp = resp.json()

    status = resp['status']
    if status != 'OK':
        if status == 'ZERO_RESULTS':
            raise _error.GoogleApiZeroResults(url, args, resp.get('error_message', 'ZERO_RESULTS'))
        elif status == 'OVER_QUERY_LIMIT':
            raise _error.GoogleApiOverQueryLimit(url, args, resp.get('error_message', 'OVER_QUERY_LIMIT'))
        elif status == 'REQUEST_DENIED':
            raise _error.GoogleApiRequestDenied(url, args, resp.get('error_message', 'REQUEST_DENIED'))
        elif status == 'INVALID_REQUEST':
            raise _error.GoogleApiInvalidRequest(url, args, resp.get('error_message', 'INVALID_REQUEST'))
        elif status == 'UNKNOWN_ERROR':
            raise _error.GoogleApiUnknownError(url, args, resp.get('error_message', 'UNKNOWN_ERROR'))

    return resp
