# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', 'portfolio.views.single',
        name='portfolio_single'),
    url(r'^$', 'portfolio.views.index', name='portfolio_index'),
]
