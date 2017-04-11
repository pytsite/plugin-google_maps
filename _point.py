"""PytSite Google Maps Plugin Location Points
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Point:
    """Abstract Point
    """
    pass


class LatLng(Point):
    """Latitude/Longitude Point
    """

    def __init__(self, lat: float, lng: float):
        self._lat = lat
        self._lng = lng

    @property
    def lat(self) -> float:
        return self._lat

    @property
    def lng(self) -> float:
        return self._lng

    def __str__(self):
        return '{},{}'.format(self._lat, self._lng)


class Address(Point):
    """Address Point.
    """

    def __init__(self, address: str):
        self._address = address

    @property
    def address(self):
        return self._address

    def __str__(self) -> str:
        return self._address
