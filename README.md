# A Python 3 library for accessing the Lichess JSON/HTTP API.

## Requirements
- Python 3
- Requests

## Quickstart
```
from lipy.client import Client

client = Client()
mekhami = client.get_user('mekhami')

print(mekhami.id)  # 'mekhami'
print(mekhami.perfs['classical']['rating'])  # '2790'    Hah. Yeah right.
```


## TODO:
- Pagination
- More useful methods on the endpoints
- Documentation
- Tests
- Packaging for PyPi

# Contributing
If you feel like contributing, feel free to open issues and/or pull requests. Any contribution is welcome :)

# Credits
The API architecture is HEAVILY inspired by the Yelp API. I straight up copied some of their methods and also their client structure. I think it's a really solid way to architect API clients that don't have dozens of endpoints or dozens of methods on those endpoints. When you only have 6-10 endpoints, having a flat, single client object API seems ideal. So, thanks Yelp for the ideas. [Yelp Python library](https://github.com/Yelp/yelp-python)
