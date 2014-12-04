# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from productos.views import *
from django.views.generic import TemplateView
from django.conf import settings
from django.views import generic
from django.views.generic import ListView
from django.views.generic import DetailView
from productos.models import Producto, Tipo, Categoria, Receta
from productos import views

urlpatterns = patterns('',

    #url(r'^$', views.dulces, name='dulces'),
    url(r'^$', views.indexMermeladas, name='index'),
    url(r'^hello.pdf$', views.HelloPDFView.as_view(), name='pdf'),


)