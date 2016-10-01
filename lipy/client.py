import inspect
import requests

from lipy.config import API_URL
from lipy.endpoints.users import UserEndpoint


class Client(object):
    _endpoints = [
        UserEndpoint,
    ]

    def __init__(self):
        self._define_request_methods()

    def _make_request(self, path, lang='en', url_params={}):
        url = 'https://{}{}{}?'.format(lang, API_URL, path)
        return requests.get(url, params=url_params)

    def _define_request_methods(self):
        endpoint_instances = [end(self) for end in self._endpoints]
        for endpoint in endpoint_instances:
            instance_methods = inspect.getmembers(endpoint, inspect.ismethod)
            self._add_instance_methods(instance_methods)

    def _add_instance_methods(self, instance_methods):
        for method in instance_methods:
            if method[0][0] is not '_':
                self.__setattr__(method[0], method[1])
