# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from productos.models import Receta, Categoria, Tipo, Producto, ImagenProducto
from django.template import RequestContext

def index(request):
    lista_de_tipos = Tipo.objects.all().order_by('nombre')
    productos = Producto.objects.all()
    context = {'lista_de_tipos': lista_de_tipos, 'productos':productos}
    return render_to_response('dulces.html',context)

