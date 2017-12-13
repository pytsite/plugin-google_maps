"""PytSite Google Maps Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import plugman as _plugman

if _plugman.is_installed(__name__):
    # Public API
    from . import _widget as widget, _point as point, _travel_mode as travel_mode, _maps as maps, \
        _geocoding as geocoding, _distance as distance, _error as error


def plugin_load():
    from pytsite import lang, tpl, router
    from plugins import assetman, permissions, settings
    from . import _settings_form, _eh

    def _browser_library_maps() -> list:
        from pytsite import lang, router
        from . import _helpers

        # Google Map API key is required
        google_url = router.url('https://maps.googleapis.com/maps/api/js', query={
            'language': lang.get_current(),
            'key': _helpers.get_google_api_key(),
            'callback': 'pytsiteGoogleMapsInit',
            'libraries': 'drawing,geometry,places,visualization',
        })

        return [
            'google_maps@js/maps.js',
            'google_maps@css/maps.css',
            (google_url, 'js', True, True),
        ]

    # Resources
    lang.register_package(__name__)
    lang.register_global('google_maps_admin_settings_url', lambda language, args: settings.form_url('google_maps'))
    tpl.register_global('google_maps_map_link', maps.link)

    assetman.register_package(__name__)
    assetman.js_module('google-maps', __name__ + '@js/google-maps')
    assetman.js_module('google-maps-widget-address-input', __name__ + '@js/google-maps-widget-address-input')
    assetman.js_module('google-maps-widget-static-map', __name__ + '@js/google-maps-widget-static-map')
    assetman.t_less(__name__)
    assetman.t_js(__name__)
    assetman.t_copy_static(__name__)

    # Permissions
    permissions.define_permission('google_maps.settings.manage', 'google_maps@manage_google_maps_settings', 'app')

    # Settings
    settings.define('google_maps', _settings_form.Form, 'google_maps@google_maps', 'fa fa-map',
                    'google_maps.settings.manage')

    # Event handlers
    router.on_dispatch(_eh.on_router_dispatch)
