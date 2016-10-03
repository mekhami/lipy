import inspect
import requests

from lipy.config import API_URL, PGN_URL
from lipy.endpoints.users import UserEndpoint
from lipy.endpoints.games import GameEndpoint
from lipy.endpoints.tournaments import TournamentEndpoint
from lipy.errors import APIRateLimitError


class Client(object):
    _endpoints = [
        UserEndpoint,
        TournamentEndpoint,
        GameEndpoint,
    ]

    def __init__(self):
        self._define_request_methods()

    def _make_request(self, path, lang='en', url_params={}):
        url = 'https://{}{}{}?'.format(lang, API_URL, path)
        response = requests.get(url, params=url_params)
        if response.status_code == 429:
            raise APIRateLimitError(
                "Exceed the API Rate limit. Please wait 60 seconds before your next request."
            )
        else:
            return response

    def _make_pgn_request(self, path, lang='en', url_params={}):
        url = 'https://{}{}{}'.format(lang, PGN_URL, path)
        return requests.get(url, params=url_params, stream=True)

    def _define_request_methods(self):
        endpoint_instances = [end(self) for end in self._endpoints]
        for endpoint in endpoint_instances:
            instance_methods = inspect.getmembers(endpoint, inspect.ismethod)
            self._add_instance_methods(instance_methods)

    def _add_instance_methods(self, instance_methods):
        for method in instance_methods:
            if method[0][0] is not '_':
                self.__setattr__(method[0], method[1])
