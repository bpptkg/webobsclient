class BasicAuthenticationAPI(object):
    """
    Basic HTTP authentication API. It uses username and password to authenticate
    a request to a server.
    """

    host = None
    username = None
    password = None
    base_path = None
    protocol = 'http'
    name = 'Basic Authentication API'

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __str__(self):
        return '<{}>(username={}, password=***)'.format(
            self.__class__.__name__,
            self.username,
        )
