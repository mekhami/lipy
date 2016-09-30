import inspect
import requests

from config import API_URL
from endpoints.users import User


class Client(object):
    _endpoints = [
        User,
    ]

    def _make_request(self, lang='en', url_params={}):
        url = 'https://{0}?'.format(API_URL.format(lang))
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


class ResponseObject(object):
    _fields = []

    def __init__(self, response):
        for field in self._fields:
            value = response[field] if field in response else None
            self.__setattr__(field, value)

    def _parse(self, field_name, cls_name, response):
        if response and field_name in response:
            if type(response[field_name]) is list:
                self._parse_list_to_objects(field_name, cls_name, response)
            else:
                self._parse_one_to_object(field_name, cls_name, response)
        else:
            self.__setattr__(field_name, None)

    def _parse_list_to_objects(self, field_name, cls_name, response):
        self.__setattr__(
            field_name,
            [cls_name(field) for field in response[field_name]]
        )

    def _parse_one_to_object(self, field_name, cls_name, response):
        self.__setattr__(
            field_name,
            cls_name(response[field_name])
        )

    def _parse_main_response_body(self, field_name, cls_name, response):
        self.__setattr__(field_name, cls_name(response))
