import unittest
from webobsclient import utils
from webobsclient.models import DataModel


class ObjectCreationTest(unittest.TestCase):

    def setUp(self):
        self.data = [
            {
                'eventid': '2019-10#1',
                'eventdate': '2019-10-02 01:41:31.36',
                'duration': '10.36'
            },
            {
                'eventid': '2019-10#2',
                'eventdate': '2019-10-02 04:20:59.68',
                'duration': '14.84'
            },
        ]

    def test_object_from_list(self):
        data_as_object = utils.object_from_list(self.data)
        for event, item in zip(data_as_object, self.data):
            self.assertEqual(event.eventid, item['eventid'])
            self.assertEqual(event.eventdate, item['eventdate'])
            self.assertEqual(event.duration, item['duration'])

    def test_object_from_dictionary(self):
        data_as_object = DataModel.object_from_dictionary(self.data[0])
        self.assertEqual(data_as_object.eventid, self.data[0]['eventid'])
        self.assertEqual(data_as_object.eventdate, self.data[0]['eventdate'])
        self.assertEqual(data_as_object.duration, self.data[0]['duration'])

        self.assertEqual(DataModel.object_from_dictionary(None), '')
