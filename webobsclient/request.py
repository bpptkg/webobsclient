import pandas as pd
import six
from httplib2 import Http
from six.moves.urllib.parse import urlencode


def encode_string(value):
    return value.encode('utf-8') \
        if isinstance(value, six.text_type) else str(value)


class BasicRequest(object):
    """
    Basic HTTP request class.
    """

    def __init__(self, api):
        self.api = api

    def _full_url(self, path):
        return '{protocol}://{host}{base_path}{path}'.format(
            protocol=self.api.protocol,
            host=self.api.host,
            base_path=self.api.base_path,
            path=path)

    def _full_url_with_params(self, path, params):
        return '{full_url}{full_query_with_params}'.format(
            full_url=self._full_url(path),
            full_query_with_params=self._full_query_with_params(params))

    def _full_query_with_params(self, params):
        params = '?{}'.format(urlencode(params)) if params else ''
        return params

    def _post_body(self, params):
        return urlencode(params)

    def url_for_get(self, path, parameters):
        return self._full_url_with_params(path, parameters)

    def get_request(self, path, **kwargs):
        return self.make_request(self.prepare_request('GET', path, kwargs))

    def post_request(self, path, **kwargs):
        return self.make_request(self.prepare_request('POST', path, kwargs))

    def prepare_request(self, method, path, params):
        url = None
        body = None
        headers = {}

        if method == 'POST':
            body = self._post_body(params)
            headers = {'Content-type': 'application/x-www-form-urlencoded'}
            url = self._full_url(path)
        else:
            url = self._full_url_with_params(path, params)

        return url, method, body, headers

    def make_request(self, url, method='GET', body=None, headers=None):
        headers = headers or {}

        if 'User-Agent' not in headers:
            headers.update(
                {'User-Agent': '{} Python Client'.format(self.api.name)})
        http_obj = Http() if six.PY3 else Http(disable_ssl_certificate_validation=True)
        http_obj.add_credentials(self.api.username, self.api.password)
        return http_obj.request(url, method, body=body, headers=headers)


class RequestMethod(object):
    """
    Base request method class.

    Request method defines how a client interact with a server. Some examples
    include what is the URL base path, available query lookup parameters, etc.
    """

    path = None
    method = 'GET'

    def __init__(self, api):
        self.api = api
        self.parameters = {}

    def _build_parameters(self, kwargs):
        for key, value in six.iteritems(kwargs):
            if value is None:
                continue
            self.parameters[key] = encode_string(value)

    def _do_api_request(self, url, method='GET', body=None, headers=None):
        headers = headers or {}
        response, content = BasicRequest(self.api).make_request(
            url, method=method, body=body, headers=headers)
        return response, content

    def prepare_request(self, **kwargs):
        self._build_parameters(kwargs)

        url, method, body, headers = BasicRequest(self.api).prepare_request(
            self.method, self.path, self.parameters)
        return url, method, body, headers

    def request(self, **kwargs):
        url, method, body, headers = self.prepare_request(**kwargs)
        response, content = self._do_api_request(url, method, body, headers)
        return response, content


class MC3RequestMethod(RequestMethod):
    """
    Base WebObs MC3 request method.
    """

    path = '/mc3.pl'
    accepts_parameters = (
        'mc',
        'y1', 'm1', 'd1', 'h1',
        'y2', 'm2', 'd2', 'h2',
        'type',
        'duree',
        'amplitude',
        'ampoper',
        'located',
        'locstatus',
        'hideloc',
        'obs',
        'graph',
        'slt',
        'newts',
        'dump',
        'trash',
        'starttime',
        'endtime',
    )
    aliases = {
        'starttime': {
            'y1': 'year',
            'm1': 'month',
            'd1': 'day',
            'h1': 'hour',
        },
        'endtime': {
            'y2': 'year',
            'm2': 'month',
            'd2': 'day',
            'h2': 'hour',
        },
    }

    def deconstruct_datetime(self, name, timestamp):
        alias = self.aliases[name]
        return {
            key: getattr(timestamp, value) for key, value in alias.items()
        }

    def _build_parameters(self, kwargs):
        alias = ['starttime', 'endtime']
        for item in alias:
            value = kwargs.pop(item, None)
            if value:
                timestamp = pd.to_datetime(value)
                kwargs.update(self.deconstruct_datetime(item, timestamp))

        for key, value in six.iteritems(kwargs):
            if value is None:
                continue
            self.parameters[key] = encode_string(value)


class Sefran3RequestMethod(RequestMethod):
    """
    Base WebObs Sefran3 request method.
    """

    path = '/sefran3.pl'
    accepts_parameters = (
        's3',
        'mc3',
        'id',
        'header',
        'status',
        'limit',
        'ref',
        'yref',
        'mref',
        'dref',
        'date',
        'high',
    )
