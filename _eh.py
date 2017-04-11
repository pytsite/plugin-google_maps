"""PytSite Google Maps Plugin Event Handlers
"""
from pytsite import auth as _auth, lang as _lang, router as _router
from . import _helpers, _errors

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """'pytsite.router.dispatch' event handler.
    """
    if _auth.get_current_user().has_permission('google_maps.settings.manage'):
        try:
            _helpers.get_google_api_key()
        except _errors.GoogleApiKeyNotDefined:
            _router.session().add_warning_message(_lang.t('google_maps@plugin_setup_required_warning'))
