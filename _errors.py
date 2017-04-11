"""PytSite Google Maps Plugin Errors
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class GoogleApiKeyNotDefined(Exception):
    pass


class GoogleApiResponseError(Exception):
    pass


class DistanceCalculationError(Exception):
    pass
