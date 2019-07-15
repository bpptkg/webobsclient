class BasicAuthenticationAPI(object):

    host = None
    username = None
    password = None
    base_path = None
    protocol = 'http'
    name = 'Basic Authentication API'

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    