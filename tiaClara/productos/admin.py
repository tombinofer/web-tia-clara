# -*- coding: utf-8 -*-
from django.contrib import admin
from productos.models import Receta, Categoria, Tipo, Producto
from django import forms

#################### Inline ####################################

#class ImagenProductoInline(admin.TabularInline):
#                         #(admin.StackedInline) me aparecen uno debajo del otro
#    extra = 3    # Aqui ndicamos la cantidad de "slots" que hay de elecciones, el 
#                 # usuario puede agregar más si lo necesita
class ProductoInline(admin.TabularInline):
    #(admin.StackedInline) me aparecen uno debajo del otro
    model = Producto
    extra = 3


###################  Admins Configurables  #############################
class ProductoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nombre']}),
        (None,               {'fields': ['tipos']}),
        (u'Categorias', {'fields': ['productos_categorias']}),
        (None, {'fields': ['productos_recetas']}),
    ]

    filter_horizontal = ['productos_categorias','productos_recetas'] #para dar un filtro horizontal para mostrar relaciones ManyToManyField                            
    list_display = ('nombre','tipos',)

    list_filter = ('productos_categorias','tipos')
    search_fields = ['nombre']

class TipoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nombre']}),
    ]
    inlines = ProductoInline

###################  Registro de Modelos al Admin   #################


admin.site.register(Receta)
admin.site.register(Categoria)
admin.site.register(Tipo)
admin.site.register(Producto, ProductoAdmin)


# Register your models here.
