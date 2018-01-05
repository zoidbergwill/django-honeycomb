=============================
django_honeycomb
=============================

.. image:: https://badge.fury.io/py/django-honeycomb.svg
    :target: https://badge.fury.io/py/django-honeycomb

.. image:: https://travis-ci.org/zoidbergwill/django-honeycomb.svg?branch=master
    :target: https://travis-ci.org/zoidbergwill/django-honeycomb

.. image:: https://codecov.io/gh/zoidbergwill/django-honeycomb/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/zoidbergwill/django-honeycomb

Django middleware for Honeycomb integration

Documentation
-------------

The full documentation is at https://django-honeycomb.readthedocs.io.

Quickstart
----------

Install django_honeycomb::

    pip install django-honeycomb

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_honeycomb.apps.DjangoHoneycombConfig',
        ...
    )

Add django_honeycomb's URL patterns:

.. code-block:: python

    from django_honeycomb import urls as django_honeycomb_urls


    urlpatterns = [
        ...
        url(r'^', include(django_honeycomb_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
