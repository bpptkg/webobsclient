import io

import pandas as pd

from .schemas import MC3Schema
from .utils import object_from_list


def decode_bytes(data):
    try:
        return data.decode('utf-8')
    except (UnicodeDecodeError, AttributeError):
        return data


class BaseParser(object):
    """
    Base parser object.
    """


class MC3Parser(BaseParser):
    """
    MC3 CSV parser object.

    It parses CSV content from web request or directly from CSV file. It also
    has an option to convert datetime type from native UTC to local time zone,
    i.e. Asia/Jakarta.
    """

    def __init__(self,
                 utc=True,
                 local_tz='Asia/Jakarta',
                 as_local_tz=False,
                 stringify_datetime=False,
                 calc_missing_fields=True,
                 datetime_format='iso-8601',
                 schema=None):
        """
        :param utc: True if WebObs MC3 bulletin datetime fields use UTC time
        zone.

        :type utc: bool

        :param local_tz: Local time zone name. Default to Asia/Jakarta.

        :type local_tz: str

        :param as_local_tz: True if you want to convert datetime fields in the
        parsed csv to local time zone.

        :type as_local_tz: bool

        :param stringify_datetime: Convert datetime fields to string if True.
        Otherwise, use native Pandas Timestamp. Default to True.

        :type stringify_datetime: bool

        :param calc_missing_fields: If true, the parser will calculate necessary
        fields to match Bulletin model columns/fields. Default to True.

        :type calc_missing_fields: bool

        :param datetime_format: When stringify_datetime is True, convert
        datetime fields to this format. Default to iso-8601.

        :type datetime_format: str

        :param schema: Uses custom schema class instead of default provided. It
        is useful if WebObs MC3 format changed and the library haven't updated
        the schema yet.

        :type schema: :class:`webobsclient.schemas.MC3Schema`
        """
        self.utc = utc
        self.local_tz = local_tz
        self.as_local_tz = as_local_tz
        self.stringify_datetime = stringify_datetime
        self.datetime_format = datetime_format
        self.calc_missing_fields = calc_missing_fields

        if schema is not None:
            self.schema = schema
        else:
            self.schema = MC3Schema()

    def to_df(self, csv):
        """
        Convert to Pandas DataFrame.
        """
        try:
            path_or_buffer = csv.decode('utf-8')
            buffer = io.StringIO(path_or_buffer)
            lines = []
            while True:
                line = buffer.readline()
                if not line:
                    break
                if not line.startswith(self.schema.comment):
                    lines.append(line)
            data = ''.join(lines)
        except (UnicodeDecodeError, AttributeError):
            path_or_buffer = csv
            lines = []
            with open(path_or_buffer, 'r') as buffer:
                while True:
                    line = buffer.readline()
                    if not line:
                        break
                    if not line.startswith(self.schema.comment):
                        lines.append(line)
            data = ''.join(lines)

        # TODO(indra): Soft index searching to determine which order of column
        # name of MC3 CSV data. It enables smart searching in case MC3 CSV
        # column order changed or one of them removed.
        df = pd.read_csv(io.StringIO(data), delimiter=self.schema.delimiter,
                         header=None, names=self.schema.get_columns())

        for col, dtype in self.schema.get_dtypes().items():
            if dtype.startswith('datetime'):
                df[col] = pd.to_datetime(df[col], utc=self.utc)
                if self.as_local_tz:
                    df[col] = df[col].dt.tz_convert(self.local_tz)

                if self.calc_missing_fields:
                    df['{}_microsecond'.format(col)] = df[col].apply(
                        lambda x: x.microsecond/10000)

                    df['valid'] = 0

                if self.stringify_datetime:
                    if (self.datetime_format == 'iso-8601'
                            or self.datetime_format == 'iso'):
                        df[col] = df[col].apply(lambda item: item.isoformat())
                    else:
                        df[col] = df[col].dt.strftime(self.datetime_format)

        return df

    def to_dataframe(self, csv):
        """
        Convert to Pandas DataFrame.
        """
        return self.to_df(csv)

    def to_dict(self, csv):
        """
        Convert to Python dictionary.
        """
        df = self.to_df(csv)
        return df.to_dict(orient='records')

    def to_dictionary(self, csv):
        """
        Convert to Python dictionary.
        """
        df = self.to_df(csv)
        return df.to_dict(orient='records')

    def to_json(self, csv):
        """
        Convert to JSON string.
        """
        df = self.to_df(csv)
        return df.to_json(orient='records')

    def to_obj(self, csv):
        """
        Convert to Python object.
        """
        data = self.to_dict(csv)
        return object_from_list(data)

    def to_object(self, csv):
        """
        Convert to Python object.
        """
        data = self.to_dict(csv)
        return object_from_list(data)
