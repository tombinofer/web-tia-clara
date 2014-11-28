# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from productos.views import *
from django.views.generic import TemplateView
from django.conf import settings
from django.views import generic
from django.views.generic import ListView
from django.views.generic import DetailView
from contenidos.models import Pagina, Imagen
from contenidos import views

urlpatterns = patterns('',

    #url(r'^$', views.dulces, name='dulces'),
    url(r'^$', views.nosotros, name='index'),

)