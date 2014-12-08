# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20141125_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='productos_recetas',
        ),
        migrations.DeleteModel(
            name='Receta',
        ),
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
