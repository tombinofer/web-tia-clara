# -*- coding: utf-8 -*-
from django.db import models


class Receta(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(help_text="Redacta una descripción")
    def __unicode__(self):              # __str__ en Python 3
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    def __unicode__(self):              # __str__ en Python 3
        return self.nombre

class Tipo(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):              # __str__ en Python 3
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    productos_categorias = models.ManyToManyField(Categoria, verbose_name = u"Categorias")
    productos_recetas = models.ManyToManyField(Receta, null=True, blank=True, verbose_name = u"Recetas")
    tipos = models.ForeignKey(Tipo)
    imagen_banner = models.ImageField(upload_to = "imgProducto")
    imagen_producto = models.ImageField(upload_to = "imgProducto")
    def __unicode__(self):              # __str__ en Python 3
        return self.nombre
   
    