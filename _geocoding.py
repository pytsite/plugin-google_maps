""" PytSite Google Maps Plugin GeoCoding
"""
import requests as _requests
from pytsite import lang as _lang
from . import _helpers, _point, _error

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

_GOOGLE_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'


def _do_request(args: dict) -> dict:
    args.update({
        'key': _helpers.get_google_api_key(),
        'language': _lang.get_current(),
    })

    resp = _requests.get(_GOOGLE_API_URL, args)

    if not resp.ok:
        raise _error.GoogleApiError(_GOOGLE_API_URL, args, resp.content.decode('utf-8'))

    resp = resp.json()

    if resp['status'] == 'OK':
        return resp
    elif resp['status'] == 'ZERO_RESULTS':
        raise _error.GoogleApiZeroResults(_GOOGLE_API_URL, args, resp.get('error_message', 'ZERO_RESULTS'))
    elif resp['status'] == 'OVER_QUERY_LIMIT':
        raise _error.GoogleApiOverQueryLimit(_GOOGLE_API_URL, args, resp.get('error_message', 'OVER_QUERY_LIMIT'))
    elif resp['status'] == 'REQUEST_DENIED':
        raise _error.GoogleApiRequestDenied(_GOOGLE_API_URL, args, resp.get('error_message', 'REQUEST_DENIED'))
    elif resp['status'] == 'INVALID_REQUEST':
        raise _error.GoogleApiInvalidRequest(_GOOGLE_API_URL, args, resp.get('error_message', 'INVALID_REQUEST'))
    elif resp['status'] == 'UNKNOWN_ERROR':
        raise _error.GoogleApiUnknownError(_GOOGLE_API_URL, args, resp.get('error_message', 'UNKNOWN_ERROR'))


def encode(address: _point.Address, first: bool = False):
    """Encode an address
    """
    r = _do_request({'address': address.address})['results']

    if first:
        return r[0] if r else None

    return r


def decode(location: _point.LatLng, first: bool = False):
    """Decode a location
    """
    r = _do_request({'latlng': '{},{}'.format(location.lat, location.lng)})['results']

    if first:
        return r[0] if r else None

    return r
