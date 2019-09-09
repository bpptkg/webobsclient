# webobsclient

WebObs Python client library.

## Installation

**webobsclient** is available on PyPI, you can install it by typing this
command:

    pip install -U webobsclient

## Requirements

* Python 3.5+
* httplib2
* six

## Making Requests

You need to specify `username` and `password` credentials of your WebObs access
login in order to make a request. For example:

```python
import webobsclient

client = webobsclient.MC3Client(username='USER', password='PASSWORD')
response, content = client.request(
    slt=0, y1=2019, m1=6, d1=15, h1=0, y2=2019, m2=7, d2=15, h2=4, type='ALL',
    duree='ALL', ampoper='eq', amplitude='ALL', locstatus=0, located=0,
    mc='MC3', dump='bul', graph='movsum')

print(response)
print(content)
```

Another example for Sefran3 client:

```python
import webobsclient

client = webobsclient.Sefran3Client(username='USER', password='PASSWORD')
response, content = client.request(
    s3='SEFRAN', mc3='MC3', date='201907150829', id=550)

print(response)
print(content)
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
