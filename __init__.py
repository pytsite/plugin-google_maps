"""PytSite Google Maps Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import plugman as _plugman

if _plugman.is_installed(__name__):
    # Public API
    from . import _widget as widget, _types as types, _travel_mode as travel_mode, _maps as maps, \
        _geocoding as geocoding, _distance as distance, _error as error, _timezone as timezone


def plugin_load_uwsgi():
    from pytsite import lang, tpl, router
    from plugins import permissions, settings
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__)
    lang.register_global('google_maps_admin_settings_url', lambda language, args: settings.form_url('google_maps'))
    tpl.register_global('google_maps_map_link', maps.link)

    # Permissions
    permissions.define_permission('google_maps@manage_settings', 'google_maps@manage_google_maps_settings', 'app')

    # Settings
    settings.define('google_maps', _settings_form.Form, 'google_maps@google_maps', 'fa fa-map',
                    'google_maps@manage_settings')

    # Event handlers
    router.on_dispatch(_eh.on_router_dispatch)
