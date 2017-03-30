"""PytSite Google Maps Plugin Event Handlers.
"""
from pytsite import auth as _auth, lang as _lang, router as _router, settings as _settings, reg as _reg

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """'pytsite.router.dispatch' event handler.
    """
    if _auth.get_current_user().has_permission('google_maps.settings.manage'):
        if not (_settings.get('google_maps.client_key') or _reg.get('google_maps.client_key')):
            _router.session().add_warning_message(_lang.t('google_maps@plugin_setup_required_warning'))
