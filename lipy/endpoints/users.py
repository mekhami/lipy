from lipy.config import USER_PATH
from lipy.response import ResponseObject


class UserEndpoint(object):
    def __init__(self, client):
        self.client = client

    def get_user(self, username, **url_params):
        user_path = USER_PATH + '/' + username
        return UserResponse(self.client._make_request(user_path, url_params=url_params))

    def get_team_users(self, team, **url_params):
        url_params['team'] = team
        return UserResponse(self.client._make_request(USER_PATH, url_params=url_params))


class UserResponse(ResponseObject):
    pass
