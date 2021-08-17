#!/usr/bin/env python

import io
import os
import re

from setuptools import find_packages, setup

with io.open('webobsclient/version.py', 'rt', encoding='utf-8') as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)


def read(filename):
    """Read file contents."""
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='webobsclient',
    version=version,
    description='WebObs Python Client',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    license='MIT',
    install_requires=[
        'httplib2',
        'six',
        'pandas',
        'sqlalchemy',
    ],
    author='BPPTKG',
    author_email='bpptkg@esdm.go.id',
    url='https://github.com/bpptkg/webobsclient',
    zip_safe=False,
    packages=find_packages(exclude=['docs', 'tests']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
