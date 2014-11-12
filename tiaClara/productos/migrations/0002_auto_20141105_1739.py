# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='productos_recetas',
            field=models.ManyToManyField(to='productos.Receta', null=True, blank=True),
            preserve_default=True,
        ),
    ]
