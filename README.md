# webobsclient

WebObs Python client.

## Installation

**webobsclient** is available on PyPI. You can install the latest version by
typing this command:

    pip install -U webobsclient

## Making Requests

You need to specify `username` and `password` credentials of your WebObs login
access in order to make a request. For example:

```python
import webobsclient

client = webobsclient.MC3Client(username='USER', password='PASSWORD')
response, content = client.request(
    slt=0, y1=2019, m1=6, d1=15, h1=0, y2=2019, m2=7, d2=15, h2=4, type='ALL',
    duree='ALL', ampoper='eq', amplitude='ALL', locstatus=0, located=0,
    hideloc=0, mc='MC3', dump='bul', graph='movsum')

print(response)
print(content)
```

Sometimes, using `y1`, `m1`, `d1`, and `h1` options are inconvenient. You can
use `starttime`, and `endtime` options indicating the time range of your
request. For example:

```python
import webobsclient

client = webobsclient.MC3Client(username='USER', password='PASSWORD')
response, content = client.request(
    starttime='2019-06-15 12:00:00', endtime='2019-07-15 12:00:00', slt=0, type='ALL',
    duree='ALL', ampoper='eq', amplitude='ALL', locstatus=0, located=0,
    hideloc=0, mc='MC3', dump='bul', graph='movsum')

print(response)
print(content)
```

Note that `starttime` and `endtime` options are only available on `MC3Client`.

Another example for Sefran3 client:

```python
import webobsclient

client = webobsclient.Sefran3Client(username='USER', password='PASSWORD')
response, content = client.request(
    s3='SEFRAN', mc3='MC3', date='201907150829', id=550)

print(response)
print(content)
```

Note that date time in the request and WebObs are both in UTC time zone. If
you're using local time zone, you should convert it to UTC time zone before
making the request.

## Parsing MC3 CSV Bulletin

`webobsclient` provides some utility classes to enable parsing MC3 CSV from
WebObs response:

```python
import webobsclient
from webobsclient.parser import MC3Parser

client = webobsclient.MC3Client(username='USER', password='PASSWORD')

response, content = client.request(
    type='VTA', starttime='2019-10-01', endtime='2019-10-31', slt=0,
    duree='ALL', ampoper='eq', amplitude='ALL', locstatus=0, located=0,
    hideloc=0, mc='MC3', dump='bul', graph='movsum')

parser = MC3Parser(content, use_local_tz=True)
print(parser.to_dictionary())
```

The above example request `VTA` earthquake event to the WebObs MC3 bulletin from
`2019-10-01` to `2019-10-31`. We create a parser instance with
`use_local_tz=True` option. This will convert any columns with date time type
from UTC to Asia/Jakarta time zone because MC3Parser class uses Asia/Jakarta
time zone by default. Method `to_dictionary()` will convert MC3 CSV to Python
dictionary.

MC3 CSV is parsed using pre-defined columns schema. You can see the columns
schema in `webobsclient/schemas.py`.

For more information about available methods and options, see the source in
`webobsclient/parser.py`.

## Changing the WebObs Host

This package primarily used at BPPTKG to interact with our WebObs server.
Default WebObs host in library is `192.168.0.25`. If your WebObs host is
different, you can change the WebObs host as follows:

```python
import webobsclient

client = webobsclient.MC3Client(username='USER', password='PASSWORD')
client.api.host = '192.168.5.10'
```

## Supported WebObs Clients

Currently only WebObs MC3 and Sefran3 is supported. More client will be added in
the future version.

## Support

This project is maintained by Indra Rudianto. If you have any question about
this project, you can contact him at <indrarudianto.official@gmail.com>.

## License

By contributing to the project, you agree that your contributions will be
licensed under its MIT license. See
[LICENSE](https://gitlab.com/bpptkg/webobsclient/blob/master/LICENSE) for
details.
