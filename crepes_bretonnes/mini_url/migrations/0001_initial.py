# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True, verbose_name=b'URL \xc3\xa0 r\xc3\xa9duire')),
                ('code', models.CharField(max_length=6, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b"Date d'enregistrement")),
                ('pseudo', models.CharField(blank=True, max_length=255, null=True)),
                ('nb_acces', models.IntegerField(default=0, verbose_name=b"Nombre d'acc\xc3\xa8s \xc3\xa0 l'URL")),
            ],
            options={
                'verbose_name': 'Mini URL',
                'verbose_name_plural': 'Minis URL',
            },
        ),
    ]
