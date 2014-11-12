# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to=b'img', verbose_name='Im\xe1gen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(help_text='Redacta una descripci\xf3n')),
                ('imagenPrincipal', models.ImageField(upload_to=b'imgPagina', verbose_name='Im\xe1gen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='imagen',
            name='pagina',
            field=models.ForeignKey(to='contenidos.Pagina'),
            preserve_default=True,
        ),
    ]
