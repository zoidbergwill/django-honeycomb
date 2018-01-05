# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_honeycomb.urls import urlpatterns as django_honeycomb_urls

urlpatterns = [
    url(r'^', include(django_honeycomb_urls, namespace='django_honeycomb')),
]
