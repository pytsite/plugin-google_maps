"""PytSite Google Maps Plugin Timezone API
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from time import time as _time
from plugins import geo as _geo
from . import _helpers


def resolve(location: _geo.types.Location, language: str = None):
    """Resolve a time zone of a location
    """

    args = {
        'location': str(location),
        'timestamp': _time(),
    }

    return _geo.types.TimeZone(_helpers.google_api_request('timezone', args, language))
