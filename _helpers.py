"""PytSite Google Maps Plugin Helper Functions
"""
from pytsite import reg as _reg
from . import _error

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def get_google_api_key() -> str:
    """Get configured Google Maps API key.
    """
    api_key = _reg.get('google_maps.api_key')
    if not api_key:
        raise _error.GoogleApiKeyNotDefined("Setting 'google_maps.api_key' is not defined")

    return api_key
