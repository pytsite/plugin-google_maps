"""PytSite Google Maps Plugin Helper Functions
"""
from pytsite import settings as _settings, reg as _reg
from . import _errors

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def get_google_api_key() -> str:
    """Get configured Google Maps API key.
    """
    api_key = _settings.get('google_maps.server_key') or _reg.get('google_maps.server_key')
    if not api_key:
        raise _errors.GoogleApiKeyNotDefined("Setting 'google_maps.server_key' is not defined")

    return api_key
