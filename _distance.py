"""PytSite Google Maps Plugin Distance Matrix Functions
"""
import requests as _requests
from pytsite import lang as _lang, cache as _cache, util as _util
from . import _helpers, _point, _travel_mode, _errors

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

API_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json'
CACHE_TTL = 86400
_cache_pool = _cache.create_pool('google_maps.distance')


def calculate(origin: _point.Point, destination: _point.Point, mode: str = _travel_mode.DRIVING,
              language: str = None) -> dict:
    """Calculate distance between two points.
    """
    if not language:
        language = _lang.get_current()

    if not isinstance(origin, _point.LatLng):
        raise TypeError('Unsupported origin point type: {}'.format(type(origin)))

    if not isinstance(destination, _point.LatLng):
        raise TypeError('Unsupported destination point type: {}'.format(type(destination)))

    c_key = _util.md5_hex_digest('{}{}{}{}'.format(origin, destination, mode, language))
    if _cache_pool.has(c_key):
        return _cache_pool.get(c_key)

    r = _requests.get(API_URL, {
        'key': _helpers.get_google_api_key(),
        'language': language,
        'mode': mode,
        'origins': str(origin),
        'destinations': str(destination),
    })

    if not r.ok:
        raise _errors.GoogleApiResponseError('Response code from Google: {}'.format(r.status_code))

    r = r.json()

    # Check search response status
    if r['status'] != 'OK':
        raise _errors.DistanceCalculationError('Calculation status from Google:'.format(r['status']))

    # Check item status
    em = r['rows'][0]['elements'][0]

    if em['status'] != 'OK':
        raise _errors.DistanceCalculationError('Calculation status from Google:'.format(em['status']))

    response = {
        'origin_address': r['origin_addresses'][0],
        'destination_address': r['destination_addresses'][0],
        'distance': em['distance'],
        'duration': em['duration'],
    }

    return _cache_pool.put(c_key, response, CACHE_TTL)
