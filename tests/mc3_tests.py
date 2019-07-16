import unittest
import webobsclient
from webobsclient.request import encode_string


class MC3ClientTest(unittest.TestCase):

    client = webobsclient.MC3Client(username='USERNAME', password='PASSWORD')

    def test_api(self):
        self.assertEqual(self.client.api.host, '192.168.0.25')
        self.assertEqual(self.client.api.username, 'USERNAME')
        self.assertEqual(self.client.api.password, 'PASSWORD')
        self.assertEqual(self.client.api.name, 'WebObs')
        self.assertEqual(self.client.api.base_path, '/cgi-bin')
        self.assertEqual(self.client.api.protocol, 'http')

    def test_client(self):
        self.assertEqual(self.client.name, 'WebObs MC3')
        self.assertEqual(self.client.path, '/mc3.pl')
        self.assertEqual(self.client.method, 'GET')

    def test_query(self):
        url, method, body, headers = self.client.prepare_request(
            slt=0, y1=2019, m1=6, d1=15, h1=0, y2=2019, m2=7, d2=15, h2=4, type='ALL',
            duree='ALL', ampoper='eq', amplitude='ALL', locstatus=0, located=0,
            mc='MC3', dump='bul', graph='movsum')

        parameters = {key: encode_string(value) for key, value in {
            'slt': 0, 'y1': 2019, 'm1': 6, 'd1': 15, 'h1': 0, 'y2': 2019,
            'm2': 7, 'd2': 15, 'h2': 4, 'type': 'ALL', 'duree': 'ALL',
            'ampoper': 'eq', 'amplitude': 'ALL', 'locstatus': 0, 'located': 0,
            'mc': 'MC3', 'dump': 'bul', 'graph': 'movsum',
        }.items()}

        self.assertDictEqual(self.client.parameters, parameters)


if __name__ == '__main__':
    unittest.main()
