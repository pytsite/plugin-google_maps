"""PytSite Google Maps Plugins Event Handlers
"""
from pytsite import metatag as _metatag, router as _router, lang as _lang, reg as _reg
from plugins import auth as _auth

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def on_router_dispatch():
    api_key = _reg.get('google_maps.api_key')
    if api_key:
        _metatag.t_set('pytsite-google-maps-api-key', api_key)
    else:
        c_user = _auth.get_current_user()
        if c_user.has_permission('google_maps.settings.manage'):
            _router.session().add_warning_message(_lang.t('google_maps@plugin_setup_required_warning'))
