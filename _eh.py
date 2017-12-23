"""PytSite Google Maps Plugins Event Handlers
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import metatag as _metatag, router as _router, lang as _lang
from plugins import auth as _auth
from . import _helpers, _error


def on_router_dispatch():
    try:
        api_key = _helpers.get_google_api_key()
        _metatag.t_set('pytsite-google-maps-api-key', api_key)
    except _error.GoogleApiKeyNotDefined:
        if _auth.get_current_user().has_permission('google_maps.settings.manage'):
            _router.session().add_warning_message(_lang.t('google_maps@plugin_setup_required_warning'))
