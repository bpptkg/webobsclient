# webobsclient

WebObs Python client library


## Installation

Clone the project from GitLab repository server via `ssh`:

    git clone git@gitlab.com:bpptkg/webobsclient.git

or clone via `https`:

    git clone https://gitlab.com/bpptkg/webobsclient.git

Checkout to the latest stable tag:

    git fetch --tags
    git checkout tags/v<major>.<minor>.<patch>

    # Example
    git checkout tags/v0.0.1

Make Python virtual environment and activate the virtual environment:

    virtualenv -p python3 venv
    source venv/bin/activate

Install dependency packages:

    cd /path/to/bmaclient/
    pip install -r requirements.txt

Install the package:

    python setup.py install

Another options is to download archive file from GitLab repository and install
the package:

    tar -xvf webobsclient-v0.1.0.tar.gz
    cd webobsclient-v0.1.0

    pip install -r requirements.txt
    python setup.py install


## Requirements

* Python 3.5+
* httplib2
* six


## Making Requests

You need to specity `username` and `password` credentials of your WebObs access
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

Viewing client attributes and methods:

```python
import webobsclient

client = webobsclient.MC3Client(username='USER', password='PASSWORD')

# WebObs API attributes
print('WebObs server host:', client.api.host) # 192.168.0.25
print('WebObs username:', client.api.username) # USER
print('WebObs password:', client.api.password) # PASSWORD
print('WebObs API name:', client.api.name) # WebObs
print('WebObs URL base path:', client.api.base_path) # /cgi-bin
print('WebObs HTTP protocol:', client.api.protocol) # http

print('Available query parameters:', client.accepts_parameters) # List of available query params
print('Client name:', client.name) # MC3 client name: WebObs MC3
print('Client path:', client.path) # MC3 URL path: /mc3.pl
print('Client HTTP method:', client.method) # HTTP method used in request: GET

# Make a request to the WebObs server
response, content = client.request(
    slt=0, y1=2019, m1=6, d1=15, h1=0, y2=2019, m2=7, d2=15, h2=4, type='ALL',
    duree='ALL', ampoper='eq', amplitude='ALL', locstatus=0, located=0,
    mc='MC3', dump='bul', graph='movsum')

print(response) # HTTP response data stored in dictonary
print(content) # HTTP content data
print('Query parameters:', client.parameters) # URL query string stored in dictionary after 'request' method called

# Get HTTP URL, method, body, and headers data without making actual request
url, method, body, headers = client.prepare_request(
    slt=0, y1=2019, m1=6, d1=15, h1=0, y2=2019, m2=7, d2=15, h2=4, type='ALL',
    duree='ALL', ampoper='eq', amplitude='ALL', locstatus=0, located=0,
    mc='MC3', dump='bul', graph='movsum')

print('Request URL:', url)
print('Request method:', method)
print('Request body:', body)
print('Request headers:', headers)
```


## Supported WebObs Clients

Currently only WebObs MC3 and Sefran3 is supported. More client will be added
in the future version.


## Support

This project is maintained by Indra Rudianto. If you have any question about
this project, you can contact him at <indrarudianto.official@gmail.com>.


## License

By contributing to the project, you agree that your contributions will be
licensed under its MIT license.
See [LICENSE](https://gitlab.com/bpptkg/webobsclient/blob/master/LICENSE) for details.
