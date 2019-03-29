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
__version__ = '0.0.10'


class Stream(click.ParamType):
    name = 'stream'
    SUPPORTED_SCHEMES = ('http', 'https')

    def __init__(self, file_mode='r', encoding=None):
        self.file_mode = file_mode
        self.encoding = encoding

    def convert(self, value, param, ctx):
        print(ctx.obj)
        if value == '-':
            return sys.stdin
        if os.path.exists(value):
            kwargs = {}
            if self.file_mode == 'rb':
                pass
            elif self.encoding is not None and PY_VERSION != 2:
                kwargs['encoding'] = self.encoding
            elif ctx.obj and ctx.obj.get('encoding') and PY_VERSION != 2:
                kwargs['encoding'] = ctx.obj.get('encoding')
            return open(value, self.file_mode, **kwargs)
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
