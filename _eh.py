"""PytSite Google Maps Plugins Event Handlers
"""
from pytsite import settings as _settings, metatag as _metatag

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    client_key = _settings.get('google_maps.client_key')
    if client_key:
        _metatag.t_set('pytsite-google-maps-client-key', client_key)
