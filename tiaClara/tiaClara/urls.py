# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf.urls import patterns, include, url
from productos import views
from django.core.urlresolvers import reverse
from productos.models import Receta, Categoria, Tipo, Producto, ImagenProducto


urlpatterns = patterns('',

    # Examples:
    #url(r'^$', 'tiaClara.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^productos/', include('productos.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
# Texto para poner al final del <title> de cada página.
admin.site.site_title = u'Administración del sitio Web Tía Clara'

# Texto a poner en los <h1> de todas las páginas.
admin.site.site_header = u'Administrador del sitio Web Tía Clara'

# Texto a poner arriba de la página de index del admin
admin.site.index_title = u'Panel de control de Web Tía Clara'