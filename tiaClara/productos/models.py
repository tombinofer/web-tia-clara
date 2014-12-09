# -*- coding: utf-8 -*-
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField

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
    descripcion = RichTextField(help_text=u"Redacta una descripción",verbose_name = u"Maridaje o Receta!")
    productos_categorias = models.ManyToManyField(Categoria, verbose_name = u"Categorias")
    tipos = models.ForeignKey(Tipo)
    def __unicode__(self):              # __str__ en Python 3
        return self.nombre

    imagen_banner = models.ImageField(upload_to = "imgProducto")
    imagen_banner_producto = ImageSpecField(source='imagen_banner',
                                      processors=[ResizeToFill(1600, 300)],
                                      format='JPEG',
                                      options={'quality': 100})



    imagen_producto = models.ImageField(upload_to = "imgProducto")
    imagen_producto_vista = ImageSpecField(source='imagen_producto',
                                      processors=[ResizeToFill(800, 800)],
                                      format='PNG',
                                      options={'quality': 100})
    
   
    