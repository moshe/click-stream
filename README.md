# click-stream
Click option type for http/https/file inputs

## Usage
```python
import click
from click_stream import Stream


@click.command()
@click.option('--in', type=Stream())
def streamcli(inp):
    click.echo(inp.read())
```

## Supported inputs
```
# files
$ cli --in /path/to/file.txt

# stdin
$ echo input from stdin | cli --in -

# HTTP/S
$ cli http://google.com
```
