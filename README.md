# DEPRECATED

Please use [beeline-python](https://github.com/honeycombio/beeline-python)'s [Django middleware](https://github.com/honeycombio/beeline-python/blob/master/beeline/middleware/django/__init__.py) instead.

# DEPRECATED

# django\_honeycomb

[![image](https://badge.fury.io/py/django-honeycomb.svg)](https://badge.fury.io/py/django-honeycomb)

[![image](https://travis-ci.org/zoidbergwill/django-honeycomb.svg?branch=master)](https://travis-ci.org/zoidbergwill/django-honeycomb)

[![image](https://codecov.io/gh/zoidbergwill/django-honeycomb/branch/master/graph/badge.svg)](https://codecov.io/gh/zoidbergwill/django-honeycomb)

Django middleware for Honeycomb integration

## Documentation

The full documentation is at <https://django-honeycomb.readthedocs.io>.

## Quickstart

Install django\_honeycomb:

    pip install django-honeycomb

Add it to your \`INSTALLED\_APPS\`:

``` sourceCode python
INSTALLED_APPS = (
    ...
    'django_honeycomb.apps.DjangoHoneycombConfig',
    ...
)
```

Add the middleware to the end of your list of
<span class="title-ref">MIDDLEWARE\_CLASSES</span> in \`settings.py\`:

``` sourceCode python
MIDDLEWARE_CLASSES = (
  # ...
  'django_honeycomb.middleware.HoneyMiddleware',
)
```

Add django\_honeycomb's required env vars:

``` sourceCode none
HONEY_WRITE_KEY
HONEY_DATASET
```

## Features

  - TODO

## Running Tests

Does the code actually work?

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

## Credits

Tools used in rendering this
    package:

  - [Cookiecutter](https://github.com/audreyr/cookiecutter)
  - [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage)
