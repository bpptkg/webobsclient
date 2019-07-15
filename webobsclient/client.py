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


class MC3Client(WebObsBasicAuthenticationAPI, MC3RequestMethod):
    """WebObs MC3 Client."""

    name = 'WebObs MC3'

    def __init__(self, **kwargs):
        WebObsBasicAuthenticationAPI.__init__(self, **kwargs)
        auth = WebObsBasicAuthenticationAPI(**kwargs)
        MC3RequestMethod.__init__(self, auth)


class Sefran3Client(WebObsBasicAuthenticationAPI, SefranRequestMethod):
    """WebObs Sefran3 Client."""

    name = 'WebObs Sefran3'

    def __init__(self, **kwargs):
        WebObsBasicAuthenticationAPI.__init__(self, **kwargs)
        auth = WebObsBasicAuthenticationAPI(**kwargs)
        SefranRequestMethod.__init__(self, auth)
