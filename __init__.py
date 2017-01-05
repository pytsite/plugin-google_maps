"""PytSite Google Maps Plugin.
"""
from . import _widget as widget, _geocoding as geocoding
from ._api import encode, decode, map_link

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _browser_library_maps() -> list:
    from pytsite import settings, lang, router

    # Google Map API key is required
    api_key = settings.get('google_maps.client_key')
    if not api_key:
        raise RuntimeError("Setting 'google_maps.client_key' is not defined.")

    google_url = router.url('https://maps.googleapis.com/maps/api/js', query={
        'language': lang.get_current(),
        'key': api_key,
        'callback': 'pytsiteGoogleMapsInit',
        'libraries': 'drawing,geometry,places,visualization',
    })

    return [
        'google_maps@js/maps.js',
        'google_maps@css/maps.css',
        (google_url, 'js', True, True),
    ]


def _init():
    from pytsite import lang, assetman, tpl, permissions, settings, browser, events
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__, alias='google_maps')
    lang.register_global('google_maps_admin_settings_url', lambda language, args: settings.form_url('google_maps'))
    tpl.register_global('google_maps_map_link', map_link)
    assetman.register_package(__name__, alias='google_maps')
    browser.register('google-maps', _browser_library_maps)

    # Permissions
    permissions.define_permission('google_maps.settings.manage', 'google_maps@manage_google_maps_settings', 'app')

    # Settings
    settings.define('google_maps', _settings_form.Form, 'google_maps@google_maps', 'fa fa-map',
                    'google_maps.settings.manage')

    # Event handlers
    events.listen('pytsite.router.dispatch', _eh.router_dispatch)


_init()
