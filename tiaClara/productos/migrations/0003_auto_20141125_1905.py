# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20141105_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagenproducto',
            name='productos',
        ),
        migrations.DeleteModel(
            name='ImagenProducto',
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen_banner',
            field=models.ImageField(default='', upload_to=b'imgProducto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen_producto',
            field=models.ImageField(default='', upload_to=b'imgProducto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='productos_categorias',
            field=models.ManyToManyField(to='productos.Categoria', verbose_name='Categorias'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='producto',
            name='productos_recetas',
            field=models.ManyToManyField(to='productos.Receta', null=True, verbose_name='Recetas', blank=True),
            preserve_default=True,
        ),
    ]
