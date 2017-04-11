""" PytSite Google Maps Plugin GeoCoding
"""
import requests as _requests
from pytsite import lang as _lang
from . import _helpers, _point

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

_GOOGLE_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'


def encode(address: _point.Address, **kwargs):
    """Encode an address.
    """
    r = _requests.get(_GOOGLE_API_URL, {
        'key': _helpers.get_google_api_key(),
        'language': _lang.get_current(),
        'address': address.address,
    }).json()['results']

    if kwargs.get('first', True):
        return r[0] if r else None

    return r


def decode(location: _point.LatLng, first: bool = False):
    """Decode a location.
    """
    r = _requests.get(_GOOGLE_API_URL, {
        'key': _helpers.get_google_api_key(),
        'language': _lang.get_current(),
        'latlng': '{},{}'.format(location.lat, location.lng),
    }).json()['results']

    if first:
        return r[0] if r else None

    return r
