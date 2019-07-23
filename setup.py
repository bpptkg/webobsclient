#!/usr/bin/env python

import os

from distutils.core import setup
from webobsclient.version import get_version


def read(filename):
    """Read file contents."""
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='webobsclient',
    version=get_version(),
    description='WebObs Python Client Libary',
    long_description=read('README.md'),
    license='MIT',
    install_requires=['httplib2', 'six'],
    author='Indra Rudianto',
    author_email='indrarudianto.official@gmail.com',
    url='https://gitlab.com/bpptkg/webobsclient',
    zip_safe=True,
    packages=['webobsclient'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Science/Research',
        'Natural Language :: Indonesian',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
