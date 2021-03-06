# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.views import generic
from productos.models import Producto, Tipo, Categoria
from contenidos.models import Pagina, Imagen
from django.conf import settings
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.views import generic

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

def indexDulces(request):
    banner = Pagina.objects.get(nombre="Dulces")
    categoria_dulce = Categoria.objects.get(nombre="Dulces")
    productos = categoria_dulce.producto_set.all().order_by('tipos__nombre')
    return render_to_response("dulces.html",{"dulces":productos, "dulce0":productos[0], "banner":banner},context_instance=RequestContext(request))

def indexJaleas(request):
    banner = Pagina.objects.get(nombre="Jaleas")
    categoria_jalea = Categoria.objects.get(nombre="Jaleas")
    productos = categoria_jalea.producto_set.all().order_by('tipos__nombre')
    return render_to_response("jaleas.html",{"jaleas":productos, "jalea0":productos[0], "banner":banner},context_instance=RequestContext(request))

def indexCervezas(request):
    banner = Pagina.objects.get(nombre="Cervezas")
    categoria_cerveza = Categoria.objects.get(nombre="Cervezas")
    productos = categoria_cerveza.producto_set.all().order_by('tipos__nombre')
    return render_to_response("cervezas.html",{"cervezas":productos, "cerveza0":productos[0], "banner":banner},context_instance=RequestContext(request))

def indexOtros(request):
    banner = Pagina.objects.get(nombre="Otros")
    categoria_otro = Categoria.objects.get(nombre="Otros")
    productos = categoria_otro.producto_set.all().order_by('tipos__nombre')
    return render_to_response("otros.html",{"otros":productos, "otro0":productos[0], "banner":banner},context_instance=RequestContext(request))

from easy_pdf.views import PDFTemplateView

class HelloPDFView(PDFTemplateView):
    template_name = "hello.html"

    def get_context_data(self, **kwargs):
        return super(HelloPDFView, self).get_context_data(
            pagesize="A4",
            title="Productos",
            
        )
     
def handler404(request):
    return render_to_response('404.html') 

def handler500(request):
    return render_to_response('500.html') 
