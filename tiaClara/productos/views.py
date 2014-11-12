# -*- coding: utf-8 -*-
from django.http import HttpResponse

#def dulces(request):
#    lista_de_tipos = Tipo.objects.all().order_by('nombre')
#    productos = Producto.objects.all()
#    context = {'lista_de_tipos': lista_de_tipos, 'productos':productos}
#    return render_to_response('dulces.html',context)

def index(request):
    return HttpResponse(u"Hola mundo. Estás en el index de encuestas.")

