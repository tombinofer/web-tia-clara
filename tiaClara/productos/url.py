# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from productos import views

urlpatterns = patterns('',

    #url(r'^$', views.dulces, name='dulces'),
    url(r'^$', views.index, name='index'),
)