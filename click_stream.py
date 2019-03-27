import gzip
import os
import sys

import click

try:
    from urlparse import urlparse
    from urllib import urlopen
    PY_VERSION = 2
except ImportError:  # Python3
    from urllib.parse import urlparse
    from urllib.request import urlopen
    PY_VERSION = 3


__url__ = 'https://github.com/moshe/click-stream'
__version__ = '0.0.7'


class Stream(click.ParamType):
    name = 'stream'
    SUPPORTED_SCHEMES = ('http', 'https')

    def __init__(self, file_mode='r', open_kwargs=None):
        self.file_mode = file_mode
        self.open_kwargs = open_kwargs
        if open_kwargs is None:
            self.open_kwargs = {}

    def convert(self, value, param, ctx):
        if value == '-':
            return sys.stdin
        if os.path.exists(value):
            return open(value, self.file_mode, **self.open_kwargs)
        url = urlparse(value)
        if url.scheme not in self.SUPPORTED_SCHEMES:
            self.fail('%s scheme is not supported' % url.scheme)
        if url.scheme in ('http', 'https'):
            if value.endswith('.gz'):
                if PY_VERSION == 2:
                    self.fail('gz file format not supported in python 2')
                else:
                    return gzip.GzipFile(mode='r', fileobj=urlopen(value))
            return urlopen(value)
