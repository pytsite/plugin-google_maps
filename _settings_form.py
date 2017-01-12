"""PytSite Google Maps Plugin Settings Form.
"""
from pytsite import widget as _widget, lang as _lang, settings as _settings

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Form(_settings.Form):
    def _on_setup_widgets(self):
        """Hook.
        """
        self.add_widget(_widget.input.Text(
            uid='setting_client_key',
            weight=10,
            label=_lang.t('google_maps@client_key'),
            required=True,
            help=_lang.t('google_maps@client_key_setup_help'),
        ))

        self.add_widget(_widget.input.Text(
            uid='setting_server_key',
            weight=20,
            label=_lang.t('google_maps@server_key'),
            required=True,
            help=_lang.t('google_maps@server_key_setup_help'),
        ))

        super()._on_setup_widgets()
