"""PytSite Google Maps Plugin Distance Matrix Functions
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang as _lang, cache as _cache, util as _util
from plugins import geo as _geo
from . import _helpers, _travel_mode, _error

CACHE_TTL = 86400
_cache_pool = _cache.create_pool('google_maps.distance')


def calculate(origin: _geo.types.Location, destination: _geo.types.Location, mode: str = _travel_mode.DRIVING,
              language: str = None) -> dict:
    """Calculate distance between two points.
    """
    if not language:
        language = _lang.get_current()

    c_key = _util.md5_hex_digest('{}{}{}{}'.format(origin, destination, mode, language))
    if _cache_pool.has(c_key):
        return _cache_pool.get(c_key)

    args = {
        'key': _helpers.get_google_api_key(),
        'language': language,
        'mode': mode,
        'origins': str(origin),
        'destinations': str(destination),
    }

    r = _helpers.google_api_request('distancematrix', args)

    # Check item status
    em = r['rows'][0]['elements'][0]

    if em['status'] != 'OK':
        raise _error.DistanceCalculationError(em['status'])

    response = {
        'origin_address': r['origin_addresses'][0],
        'destination_address': r['destination_addresses'][0],
        'distance': em['distance'],
        'duration': em['duration'],
    }

    return _cache_pool.put(c_key, response, CACHE_TTL)
