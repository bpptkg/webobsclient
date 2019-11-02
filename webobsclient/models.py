import six


class ApiModel(object):
    """
    Base API model class.
    """

    @classmethod
    def object_from_dictionary(cls, entry):
        if entry is None:
            return ''
        entry_dict = dict([
            (str(key), value) for key, value in entry.items()
        ])
        return cls(**entry_dict)


class DataModel(ApiModel):
    """
    Data model class. It takes a list of dictionary and holds them as object.
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)
