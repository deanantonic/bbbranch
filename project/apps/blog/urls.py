# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [



    
    url(
        r'^blog/view/(?P<slug>[^\.]+).html', 
        'blog.views.view_post', 
        name='view_blog_post'),
    url(
        r'^blog/category/(?P<slug>[^\.]+).html', 
        'blog.views.view_category', 
        name='view_blog_category'),
    url(r'^$', 'blog.views.index', name='blog_index'),





]
