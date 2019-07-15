class APIClientError(Exception):

    def __init__(self, error_message, status_code=None):
        self.status_code = status_code
        self.error_message = error_message


class APIError(Exception):

    def __init__(self, status_code, error_type, error_message, *args, **kwargs):
        self.status_code = status_code
        self.error_type = error_type
        self.error_message = error_message
