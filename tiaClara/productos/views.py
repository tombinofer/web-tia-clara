# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.views import generic
from productos.models import Receta, Producto, Tipo, Categoria
from contenidos.models import Pagina, Imagen
from django.conf import settings
from productos.forms import ContactoForm
from django.core.mail import EmailMessage
from django.template import RequestContext

#def dulces(request):
#    lista_de_tipos = Tipo.objects.all().order_by('nombre')
#    productos = Producto.objects.all()
#    context = {'lista_de_tipos': lista_de_tipos, 'productos':productos}
#    return render_to_response('dulces.html',context)

def indexMermeladas(request):
    banner = Pagina.objects.get(nombre="Mermeladas")
    categoria_mermelada = Categoria.objects.get(nombre="Mermeladas")
    productos = categoria_mermelada.producto_set.all().order_by('tipos__nombre')
    return render_to_response("mermeladas.html",{"mermeladas":productos, "mermelada0": productos[0], "banner":banner}, context_instance=RequestContext(request))


def lista_paginas(request):
    paginas = Pagina.objects.all()
    return render_to_response("contacto.html",{"paginas":paginas}, context_instance=RequestContext(request))




    
#def contacto(request):
#        formContact = ContactoForm(request.POST)
#        if formContact.is_valid():
#            titulo = 'Sitio Web Tía Clara - Producto Artesanal :'
#            contenido = formContact.cleaned_data['nombre'] + "\n" + formContact.cleaned_data['mensaje'] + "\n"
#            contenido += 'Comunicarse a: ' + formContact.cleaned_data['correo']
#            correo = EmailMessage(titulo, contenido, to=['webtiaclara@gmail.com'], headers={'Reply-To': formContact.cleaned_data['correo']})
#            correo.send()
#            return HttpResponseRedirect('/')
#        formContact = ContactoForm()
#    return render_to_response("contacto.html",{"formContact":formContact}, context_instance=RequestContext(request))

