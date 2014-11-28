# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenidos', '0002_auto_20141112_1807'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagen',
            options={'verbose_name_plural': 'Im\xe1genes De la P\xe1gina!'},
        ),
        migrations.AlterField(
            model_name='pagina',
            name='descripcion',
            field=ckeditor.fields.RichTextField(help_text='Redacta una descripci\xf3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagina',
            name='imagenPrincipal',
            field=models.ImageField(upload_to=b'imgPagina', verbose_name='Banner de la P\xe1gina!'),
            preserve_default=True,
        ),
    ]
