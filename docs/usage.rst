=====
Usage
=====

To use django_honeycomb in a project, add it to your `INSTALLED_APPS`:

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
