class BaseSchema(object):
    """
    Base columns schema.
    """
    pass


class MC3Schema(BaseSchema):
    """WebObs MC3 CSV schema."""

    delimiter = ';'
    comment = '#'
    schema = [
        {
            'name': 'eventdate',
            'type': 'datetime64[s]'
        },
        {
            'name': 'number',
            'type': 'int32',
        },
        {
            'name': 'duration',
            'type': 'float32',
        },
        {
            'name': 'amplitude',
            'type': 'float32',
        },
        {
            'name': 'magnitude',
            'type': 'float32',
        },
        {
            'name': 'longitude',
            'type': 'float32',
        },
        {
            'name': 'latitude',
            'type': 'float32',
        },
        {
            'name': 'depth',
            'type': 'float32',
        },
        {
            'name': 'type',
            'type': 'str',
        },
        {
            'name': 'file',
            'type': 'str',
        },
        {
            'name': 'locmode',
            'type': 'str',
        },
        {
            'name': 'loctype',
            'type': 'str',
        },
        {
            'name': 'projection',
            'type': 'str',
        },
        {
            'name': 'operator',
            'type': 'str',
        },
        {
            'name': 'timestamp',
            'type': 'datetime64[s]',
        },
        {
            'name': 'eventid',
            'type': 'str',
        },
    ]

    @property
    def columns(self):
        """Return column names of MC3 CSV schema."""
        return [item['name'] for item in self.schema]

    @property
    def types(self):
        """Return column type of MC3 CSV schema."""
        return [item['type'] for item in self.schema]

    @classmethod
    def get_columns(self):
        """
        Get MC3 schema columns.
        """
        return [item['name'] for item in self.schema]

    @classmethod
    def get_types(self):
        """
        Get MC3 schema types.
        """
        return [item['type'] for item in self.schema]

    @classmethod
    def get_dtypes(self):
        """
        Get MC3 schema dtypes.
        """
        return {item['name']: item['type'] for item in self.schema}
