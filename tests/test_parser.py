import os
import csv
import json
import unittest

from webobsclient.parser import MC3Parser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURES_DIR = os.path.join(BASE_DIR, 'fixtures')


def read_csv_as_string(path):
    with open(path, 'rb') as buffer:
        data = buffer.read()
    return data


class MC3ParserTest(unittest.TestCase):

    def setUp(self):
        path = os.path.join(FIXTURES_DIR, 'MC3_dump_bulletin.csv')
        self.csv = [
            path,
            read_csv_as_string(path)
        ]

    def test_parser(self):
        for path in self.csv:
            parser = MC3Parser(path)
            self.assertEqual(len(parser.to_dataframe()), 615)

    def test_parser_stringify_datetime(self):
        for path in self.csv:
            parser = MC3Parser(path)
            for _, row in parser.to_dataframe().iterrows():
                self.assertTrue(isinstance(row['eventdate'], str))

    def test_parser_utc_to_local_conversion(self):
        for path in self.csv:
            parser = MC3Parser(path, use_local_tz=True)
            data = parser.to_dataframe()
            self.assertEqual(data['eventdate'][0],
                             '2019-10-02T08:41:31.840000+07:00')
            self.assertEqual(data['eventdate'][1],
                             '2019-10-02T11:20:59.680000+07:00')
            self.assertEqual(data['eventdate'][2],
                             '2019-10-02T12:00:02+07:00')
            self.assertEqual(data['eventdate'][3],
                             '2019-10-02T15:12:38.600000+07:00')
            self.assertEqual(data['eventdate'][4],
                             '2019-10-02T18:07:44.760000+07:00')

    def test_parser_to_dictionary(self):
        for path in self.csv:
            parser = MC3Parser(path)
            data = parser.to_dictionary()
            self.assertEqual(data[0]['eventdate'],
                             '2019-10-02T01:41:31.840000+00:00')
            self.assertEqual(data[1]['eventdate'],
                             '2019-10-02T04:20:59.680000+00:00')
            self.assertEqual(data[2]['eventdate'],
                             '2019-10-02T05:00:02+00:00')
            self.assertEqual(data[3]['eventdate'],
                             '2019-10-02T08:12:38.600000+00:00')
            self.assertEqual(data[4]['eventdate'],
                             '2019-10-02T11:07:44.760000+00:00')

    def test_parser_to_json(self):
        for path in self.csv:
            parser = MC3Parser(path)
            data = parser.to_json()
            json_data = json.loads(data)
            self.assertEqual(json_data[0]['eventdate'],
                             '2019-10-02T01:41:31.840000+00:00')
            self.assertEqual(json_data[1]['eventdate'],
                             '2019-10-02T04:20:59.680000+00:00')
            self.assertEqual(json_data[2]['eventdate'],
                             '2019-10-02T05:00:02+00:00')
            self.assertEqual(json_data[3]['eventdate'],
                             '2019-10-02T08:12:38.600000+00:00')
            self.assertEqual(json_data[4]['eventdate'],
                             '2019-10-02T11:07:44.760000+00:00')

    def test_parser_to_object(self):
        for path in self.csv:
            parser = MC3Parser(path)
            data = parser.to_object()
            self.assertEqual(data[0].eventdate,
                             '2019-10-02T01:41:31.840000+00:00')
            self.assertEqual(data[1].eventdate,
                             '2019-10-02T04:20:59.680000+00:00')
            self.assertEqual(data[2].eventdate,
                             '2019-10-02T05:00:02+00:00')
            self.assertEqual(data[3].eventdate,
                             '2019-10-02T08:12:38.600000+00:00')
            self.assertEqual(data[4].eventdate,
                             '2019-10-02T11:07:44.760000+00:00')


if __name__ == '__main__':
    unittest.main()
