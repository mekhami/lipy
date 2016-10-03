import pprint


class ResponseObject(object):
    def __init__(self, response):
        response = response.json()
        for field in response:
            value = response[field] if field in response else None
            self.__setattr__(field, value)

    def json(self):
        return pprint.pprint(vars(self))
