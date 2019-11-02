import six

from webobsclient.models import DataModel


def encode_string(value):
    return value.encode('utf-8') \
        if isinstance(value, six.text_type) else str(value)


def object_from_list(entry):
    """Objectify item in a list of dictionary."""
    return [DataModel(**item) for item in entry]


def rename_dictionary_key(entry, dict_map):
    """
    Rename dictionary key of particular entry.
    """
    if isinstance(entry, dict):
        for old_key, new_key in dict_map.items():
            entry[new_key] = entry.pop(old_key)
        return entry
    elif isinstance(entry, list):
        return [
            dict(
                (dict_map[old_key], value)
                if old_key in dict_map else (old_key, value)
                for old_key, value in item.items()
            )
            for item in entry
        ]
    elif isinstance(entry, tuple):
        return tuple(
            tuple(
                (dict_map[value[0]], value[1])
                if value[0] in dict_map else value
                for value in item
            )
            for item in entry
        )
