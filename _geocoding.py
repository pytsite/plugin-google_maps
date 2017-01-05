""" PytSite Google Maps GeoCoding API.
"""
import requests as _requests
from pytsite import geo as _geo, lang as _lang, settings as _settings

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class GeoCoder(_geo.interface.GeoCoder):
    def __init__(self):
        # Google Map API key is required
        self._api_key = _settings.get('google_maps.server_key')
        if not self._api_key:
            raise RuntimeError("Setting 'google_maps.server_key' is not defined.")

    def encode(self, address: str, **kwargs):
        r = _requests.get('https://maps.googleapis.com/maps/api/geocode/json', {
            'key': self._api_key,
            'language': _lang.get_current(),
            'address': address,
        }).json()['results']

        if kwargs.get('first', True):
            return r[0] if r else None

        return r

    def decode(self, lng: float, lat: float, **kwargs):
        r = _requests.get('https://maps.googleapis.com/maps/api/geocode/json', {
            'key': self._api_key,
            'language': _lang.get_current(),
            'latlng': '{},{}'.format(lat, lng),
            # 'location_type': kwargs.get('location_type', 'ROOFTOP'),
            # 'result_type': kwargs.get('result_type', 'street_address'),
        }).json()['results']

        if kwargs.get('first', True):
            return r[0] if r else None

        return r
