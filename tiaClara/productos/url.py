# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from productos import views
from productos.models import Receta, Categoria, Tipo, Producto, ImagenProducto


urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
)