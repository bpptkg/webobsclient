from .auth import BasicAuthenticationAPI
from .request import (
    BasicRequest, MC3RequestMethod, SefranRequestMethod
)

__all__ = [
    'MC3Client',
    'Sefran3Client',
]


class WebObsBasicAuthenticationAPI(BasicAuthenticationAPI):
    """WebObs Basic Authentication."""

    host = '192.168.0.25'
    base_path = '/cgi-bin'
    protocol = 'http'
    name = 'WebObs'

    def __init__(self, **kwargs):
        super(WebObsBasicAuthenticationAPI, self).__init__(**kwargs)


class MC3Client(MC3RequestMethod):
    """WebObs MC3 Client."""

    name = 'WebObs MC3'

    def __init__(self, **kwargs):
        auth = WebObsBasicAuthenticationAPI(**kwargs)
        super(MC3Client, self).__init__(auth)


class Sefran3Client(SefranRequestMethod):
    """WebObs Sefran3 Client."""

    name = 'WebObs Sefran3'

    def __init__(self, **kwargs):
        auth = WebObsBasicAuthenticationAPI(**kwargs)
        super(Sefran3Client, self).__init__(auth)
