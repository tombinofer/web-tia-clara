# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
import os
from django.views import generic
from productos import views

urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),
    url(r'^mermeladas/', include('productos.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contacto/$','productos.views.contacto'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(settings.STATIC_ROOT, 'css')}),
    url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(settings.STATIC_ROOT, 'fonts')}),
    url(r'^img/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(settings.STATIC_ROOT, 'img')}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(settings.STATIC_ROOT, 'js')}),
)
# Texto para poner al final del <title> de cada página.
admin.site.site_title = u'Administración del sitio Web Tía Clara'

# Texto a poner en los <h1> de todas las páginas.
admin.site.site_header = u'Administrador del sitio Web Tía Clara'

# Texto a poner arriba de la página de index del admin
admin.site.index_title = u'Panel de control del sitio Web Tía Clara'