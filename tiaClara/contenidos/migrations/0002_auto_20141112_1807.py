# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagen',
            options={'verbose_name_plural': 'Im\xe1genes'},
        ),
        migrations.AlterModelOptions(
            name='pagina',
            options={'verbose_name_plural': 'P\xe1ginas'},
        ),
        migrations.RenameField(
            model_name='imagen',
            old_name='pagina',
            new_name='paginas',
        ),
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(upload_to=b'img', verbose_name='Im\xe1genes'),
            preserve_default=True,
        ),
    ]
