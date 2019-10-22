import unittest
from webobsclient.utils import rename_dictionary_key


class RenameDictionaryKeyTest(unittest.TestCase):

    def test_rename_dictionary_key_with_dictionary(self):
        entry = {
            'a': 'a',
            'b': 'b',
            'c': 'c'
        }
        dict_map = {
            'a': '1',
            'b': '2'
        }
        new_entry = rename_dictionary_key(entry, dict_map)
        self.assertDictEqual(new_entry, {'1': 'a', '2': 'b', 'c': 'c'})

    def test_rename_dictionary_key_with_list(self):
        entry = [
            {
                'a': 'a',
                'b': 'b',
                'c': 'c'
            },
            {
                'a': 'a',
                'b': 'b',
                'c': 'c'
            }
        ]
        dict_map = {
            'a': '1',
            'b': '2'
        }
        new_entry = rename_dictionary_key(entry, dict_map)
        self.assertListEqual(new_entry, [
            {'1': 'a', '2': 'b', 'c': 'c'},
            {'1': 'a', '2': 'b', 'c': 'c'}
        ])

    def test_rename_dictionary_key_with_tuple(self):
        entry = (
            (
                ('a', 'a'),
                ('b', 'b'),
                ('c', 'c'),
            ),
            (
                ('a', 'a'),
                ('b', 'b'),
                ('c', 'c'),
            ),
        )
        dict_map = {
            'a': '1',
            'b': '2'
        }
        new_entry = rename_dictionary_key(entry, dict_map)
        self.assertTupleEqual(new_entry, (
            (
                ('1', 'a'),
                ('2', 'b'),
                ('c', 'c'),
            ),
            (
                ('1', 'a'),
                ('2', 'b'),
                ('c', 'c'),
            ),
        ))


if __name__ == '__main__':
    unittest.main()
