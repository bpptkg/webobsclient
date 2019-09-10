import io
import pandas as pd

from .schemas import MC3Schema
from .utils import object_from_list


def decode_bytes(data):
    try:
        return data.decode('utf-8')
    except (UnicodeDecodeError, AttributeError):
        return data


class MC3Parser(object):
    """
    MC3 CSV parser object.

    It parses CSV content from web request or directly for CSV files. It also
    has an option to convert datetime type from native UTC to local time zone,
    i.e. Asia/Jakarta.
    """

    def __init__(self,
                 csv,
                 utc=True,
                 local_tz='Asia/Jakarta',
                 use_local_tz=False,
                 stringify_datetime=True,
                 schema=None):
        self.csv = csv
        self.utc = utc
        self.local_tz = local_tz
        self.use_local_tz = use_local_tz
        self.stringify_datetime = stringify_datetime
        if schema:
            self.schema = schema
        else:
            self.schema = MC3Schema()

    def to_dataframe(self):
        """
        Convert to Pandas DataFrame.
        """
        try:
            path_or_buffer = self.csv.decode('utf-8')
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
            path_or_buffer = self.csv
            lines = [line for line in open(
                path_or_buffer) if not line.startswith(self.schema.comment)]
            data = ''.join(lines)

        # TODO(indra): Soft index searching to determine which the order of
        # column name of MC3 CSV data. It enable smart searching in case MC3 CSV
        # column order changed or one of them removed.
        df = pd.read_csv(io.StringIO(data), delimiter=self.schema.delimiter,
                         header=None, names=self.schema.get_columns())

        for col, dtype in MC3Schema.get_dtypes().items():
            if dtype.startswith('datetime'):
                df[col] = pd.to_datetime(df[col], utc=self.utc)
                if self.use_local_tz:
                    df[col] = df[col].dt.tz_convert(self.local_tz)

                if self.stringify_datetime:
                    df[col] = df[col].astype(str)

        return df

    def to_dictionary(self):
        """
        Convert to Python dictionary.
        """
        df = self.to_dataframe()
        return df.to_dict(orient='records')

    def to_json(self):
        """
        Convert to JSON string.
        """
        df = self.to_dataframe()
        return df.to_json(orient='records')

    def to_object(self):
        """
        Convert to Python object.
        """
        data = self.to_dictionary()
        return object_from_list(data)
