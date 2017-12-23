"""PytSite Google Maps Plugin Timezone API
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from time import time as _time
from . import _helpers, _types


def resolve(location: _types.Location, language: str = None):
    """Resolve a time zone of a location
    """

    args = {
        'location': str(location),
        'timestamp': _time(),
    }

    return _types.TimeZone(_helpers.google_api_request('timezone', args, language))
