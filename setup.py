from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except Exception:
    long_description = ''

setup(
    name='click-stream',
    author='Moshe Zada',
    version='0.0.1',
    keywords=['click', 'stream', 'cli', 'url'],
    url='https://github.com/Moshe/click-stream',
    py_modules=['click_stream'],
    license='',
    long_description=long_description,
    description='Click option type for http/https/file inputs',
    install_requires=[
        'click'
    ],
    tests_require=[
        'pytest'
    ]
)
