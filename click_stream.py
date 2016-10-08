import click
import os
from urlparse import urlparse
from urllib import urlopen
import sys

__url__ = 'https://github.com/moshe/click-stream'
__version__ = '0.0.1'


class Stream(click.ParamType):
    name = 'stream'
    SUPPORTED_SCHEMES = ('http', 'https')

    def __init__(self, file_mode='r'):
        self.file_mode = file_mode

    def convert(self, value, param, ctx):
        if value == '-':
            return sys.stdin
        if os.path.exists(value):
            return file(value, self.file_mode)
        url = urlparse(value)
        if url.scheme not in self.SUPPORTED_SCHEMES:
            self.fail('%s scheme is not supported' % url.scheme)
        if url.scheme in ('http', 'https'):
            return urlopen(value)
