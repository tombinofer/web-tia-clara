# -*- coding: utf-8 -*-
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField

class Pagina(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = RichTextField(help_text=u"Redacta una descripción")
    imagenPrincipal = models.ImageField(upload_to = "imgPagina", verbose_name = u"Banner de la Página!")
    imagen_pagina_principal = ImageSpecField(source='imagenPrincipal',
                                      #processors=[ResizeToFill(1351, 338)], es como la agarra el navegador!
                                      processors=[ResizeToFill(1600, 450)],
                                      format='JPEG',
                                      options={'quality': 100})

    def __unicode__(self):              # __str__ en Python 3
        return self.nombre

    class Meta:
        verbose_name_plural = 'Páginas'
        
class Imagen(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to = "img", verbose_name = u"Imágenes") 
    imagen_pagina = ImageSpecField(source='imagen',
                                      processors=[ResizeToFill(300, 300)],
                                      format='JPEG',
                                      options={'quality': 100})
    paginas = models.ForeignKey(Pagina)

    def __unicode__(self):              # __str__ en Python 3
        return self.nombre

    class Meta:
        verbose_name_plural = 'Imágenes De la Sección Nosotros'
            