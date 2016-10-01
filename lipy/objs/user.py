from lipy.endpoints.users import ResponseObject


class User(ResponseObject):
    _fields = [
        'username',
        'title',
        'url',
        'online',
        'playing',
        'engine',
        'language',
    ]
