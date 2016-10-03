from lipy.config import TOURNAMENT_PATH
from lipy.response import ResponseObject


class TournamentEndpoint(object):
    def __init__(self, client):
        self.client = client

    def get_tournament(self, tournament_id, **url_params):
        tournament_path = TOURNAMENT_PATH + '/' + tournament_id
        return TournamentResponse(self.client._make_request(tournament_path, url_params=url_params))

    def get_scheduled_tournaments(self, **url_params):
        return TournamentResponse(self.client._make_request(TOURNAMENT_PATH, url_params=url_params))


class TournamentResponse(ResponseObject):
    pass
