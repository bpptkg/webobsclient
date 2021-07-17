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
            parser = MC3Parser()
            self.assertEqual(len(parser.to_dataframe(path)), 4)

    def test_parser_stringify_datetime(self):
        for path in self.csv:
            parser = MC3Parser(stringify_datetime=True, as_local_tz=False)
            for _, row in parser.to_dataframe(path).iterrows():
                self.assertTrue(isinstance(row['eventdate'], str))

    def test_parser_utc_to_local_tz_conversion(self):
        for path in self.csv:
            parser = MC3Parser(stringify_datetime=True, as_local_tz=True)
            data = parser.to_dataframe(path)
            self.assertEqual(data['eventdate'][0],
                             '2021-07-08T07:02:00.240000+07:00')
            self.assertEqual(data['eventdate'][1],
                             '2021-07-08T07:04:19+07:00')
            self.assertEqual(data['eventdate'][2],
                             '2021-07-08T07:09:43.600000+07:00')
            self.assertEqual(data['eventdate'][3],
                             '2021-07-08T07:10:11.880000+07:00')

    def test_parser_to_dictionary(self):
        for path in self.csv:
            parser = MC3Parser(stringify_datetime=True, as_local_tz=False)
            data = parser.to_dictionary(path)
            self.assertEqual(data[0]['eventdate'],
                             '2021-07-08T00:02:00.240000+00:00')
            self.assertEqual(data[1]['eventdate'],
                             '2021-07-08T00:04:19+00:00')
            self.assertEqual(data[2]['eventdate'],
                             '2021-07-08T00:09:43.600000+00:00')
            self.assertEqual(data[3]['eventdate'],
                             '2021-07-08T00:10:11.880000+00:00')

    def test_parser_to_json(self):
        for path in self.csv:
            parser = MC3Parser(stringify_datetime=True, as_local_tz=False)
            jsonstr = parser.to_json(path)
            data = json.loads(jsonstr)
            self.assertEqual(data[0]['eventdate'],
                             '2021-07-08T00:02:00.240000+00:00')
            self.assertEqual(data[1]['eventdate'],
                             '2021-07-08T00:04:19+00:00')
            self.assertEqual(data[2]['eventdate'],
                             '2021-07-08T00:09:43.600000+00:00')
            self.assertEqual(data[3]['eventdate'],
                             '2021-07-08T00:10:11.880000+00:00')

    def test_parser_to_object(self):
        for path in self.csv:
            parser = MC3Parser(stringify_datetime=True, as_local_tz=False)
            data = parser.to_object(path)
            self.assertEqual(data[0].eventdate,
                             '2021-07-08T00:02:00.240000+00:00')
            self.assertEqual(data[1].eventdate,
                             '2021-07-08T00:04:19+00:00')
            self.assertEqual(data[2].eventdate,
                             '2021-07-08T00:09:43.600000+00:00')
            self.assertEqual(data[3].eventdate,
                             '2021-07-08T00:10:11.880000+00:00')


if __name__ == '__main__':
    unittest.main()
