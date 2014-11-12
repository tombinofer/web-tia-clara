# -*- coding: utf-8 -*-
from django.db import models

class Pagina(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(help_text=u"Redacta una descripción")
    imagenPrincipal = models.ImageField(upload_to = "imgPagina", verbose_name = u"Imágen")

    def __unicode__(self):              # __str__ en Python 3
        return self.nombre

    class Meta:
        verbose_name_plural = 'Páginas'
        
class Imagen(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to = "img", verbose_name = u"Imágenes")
    paginas = models.ForeignKey(Pagina)

    def __unicode__(self):              # __str__ en Python 3
        return self.nombre

    class Meta:
        verbose_name_plural = 'Imágenes'
            