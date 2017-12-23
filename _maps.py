"""PytSite Google Maps Plugin Map Functions
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import router as _router
from . import _types


def link(location: _types.Location, query: str = None, zoom: int = 15) -> str:
    """Get link to a map.
    """
    if query:
        return _router.url('https://www.google.com/maps/search/{}/@{},{},{}z'.
                           format(query, location.lat, location.lng, zoom))
    else:
        return _router.url('https://www.google.com/maps', query={
            'q': '{},{}'.format(location.lat, location.lng)
        })
