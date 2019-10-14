import unittest
import webobsclient
from webobsclient.request import encode_string


class QueryAliasesTest(unittest.TestCase):

    def setUp(self):
        self.client = webobsclient.MC3Client(
            username='user', password='secret')

    def test_query_alias(self):
        self.client.prepare_request(
            slt=0, starttime='2019-06-15 00:00:00',
            endtime='2019-07-15 04:00:00', type='ALL',
            duree='ALL', ampoper='eq', amplitude='ALL', locstatus=0, located=0,
            mc='MC3', dump='bul', graph='movsum'
        )

        parameters = {key: encode_string(value) for key, value in {
            'slt': 0, 'y1': 2019, 'm1': 6, 'd1': 15, 'h1': 0, 'y2': 2019,
            'm2': 7, 'd2': 15, 'h2': 4, 'type': 'ALL', 'duree': 'ALL',
            'ampoper': 'eq', 'amplitude': 'ALL', 'locstatus': 0, 'located': 0,
            'mc': 'MC3', 'dump': 'bul', 'graph': 'movsum',
        }.items()}

        self.assertDictEqual(self.client.parameters, parameters)
