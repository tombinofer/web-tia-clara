# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.views import generic
from productos.models import Receta, Producto, Tipo, Categoria
from contenidos.models import Pagina, Imagen
from django.conf import settings
from django.template import RequestContext

# Create your views here.
def nosotros(request):
    nosotros = Pagina.objects.get(nombre="Nosotros")
    return render_to_response("nosotros.html",{"nosotros": nosotros ,"imagen":nosotros.imagen_set.all()}, context_instance=RequestContext(request))

