from lipy.config import GAME_PATH
from lipy.response import ResponseObject


class GameEndpoint(object):
    def __init__(self, client):
        self.client = client

    def get_game(self, game_id, **url_params):
        game_path = GAME_PATH + '/' + game_id
        return GameResponse(self.client._make_request(game_path, url_params=url_params))

    def export_game(self, game_id, **url_params):
        game_path = GAME_PATH + '/export/' + game_id + '.pgn'
        return GamePGNResponse(self.client._make_pgn_request(game_path, url_params=url_params))


class GameResponse(ResponseObject):
    pass


class GamePGNResponse(ResponseObject):
    def __init__(self, response):
        self.pgn = response.content.decode('utf-8')
