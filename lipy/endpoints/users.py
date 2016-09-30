from .config import USER_PATH
from .client import ResponseObject


class User(object):
    def __init__(self, client):
        self.client = client

    def get_user(self, user_id, **url_params):
        return UserResponse(self.client._make_request(USER_PATH, url_params))


class UserResponse(ResponseObject):
    def __init__(self, response):
        super().__init__(response)

        self._parse_main_response_body('user', User, response)
