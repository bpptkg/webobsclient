import unittest
import webobsclient
from webobsclient.request import encode_string


class Sefran3ClientTest(unittest.TestCase):

    client = webobsclient.Sefran3Client(
        username='USERNAME', password='PASSWORD')

    def test_api(self):
        self.assertEqual(self.client.api.host, '192.168.0.25')
        self.assertEqual(self.client.api.username, 'USERNAME')
        self.assertEqual(self.client.api.password, 'PASSWORD')
        self.assertEqual(self.client.api.name, 'WebObs')
        self.assertEqual(self.client.api.base_path, '/cgi-bin')
        self.assertEqual(self.client.api.protocol, 'http')

    def test_client(self):
        self.assertEqual(self.client.name, 'WebObs Sefran3')
        self.assertEqual(self.client.path, '/sefran3.pl')
        self.assertEqual(self.client.method, 'GET')

    def test_query(self):
        url, method, body, headers = self.client.prepare_request(
            s3='SEFRAN', mc3='MC3', date='201907150829', id=550)

        parameters = {key: encode_string(value) for key, value in {
            's3': 'SEFRAN', 'mc3': 'MC3', 'date': '201907150829', 'id': 550
        }.items()}

        self.assertDictEqual(self.client.parameters, parameters)


if __name__ == '__main__':
    unittest.main()
