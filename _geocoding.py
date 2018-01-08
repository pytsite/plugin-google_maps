""" PytSite Google Maps Plugin GeoCoding
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import List as _List
from plugins import geo as _geo
from . import _helpers


def encode(address: str, components: _List[str] = None, first: bool = True, language: str = None):
    """Encode an address
    """
    args = {'address': address}
    if components:
        args.update({'components': '|'.join(components)})

    r = _helpers.google_api_request('geocode', args, language)['results']

    if first:
        return _geo.types.GeocodingResult(r[0]) if r else None

    return _geo.types.GeocodingResults(r)


def decode(location: _geo.types.Location, first: bool = True, language: str = None):
    """Decode a location
    """
    r = _helpers.google_api_request('geocode', {'latlng': str(location)}, language)['results']

    if first:
        return _geo.types.GeocodingResult(r[0]) if r else None

    return _geo.types.GeocodingResults(r)
