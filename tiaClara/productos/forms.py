# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from productos.models import Producto, Receta

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100,
                           label=(u'Tu nombre!'))

    correo = forms.EmailField(max_length=200,
                            label=(u'Tu Correo Electrónico!'))

    mensaje = forms.CharField(widget=forms.Textarea,
                            label=(u'Tu Mensaje!'))
    