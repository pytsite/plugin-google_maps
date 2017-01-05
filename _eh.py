"""PytSite Google Maps Plugin Event Handlers.
"""
from pytsite import auth as _auth, lang as _lang, router as _router, settings as _settings

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """'pytsite.router.dispatch' event handler.
    """
    if _auth.get_current_user().has_permission('google_maps.settings.manage'):
        msg = _lang.t('google_maps@plugin_setup_required_warning')
        if not _settings.get('google_maps.client_key') or not _settings.get('google_maps.server_key'):
            _router.session().add_warning_message(msg)
        else:
            _router.session().get_warning_message(msg)
