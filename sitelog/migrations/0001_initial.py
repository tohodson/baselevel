# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sitelog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stationID', models.IntegerField()),
                ('siteName', models.CharField(max_length=255)),
                ('water', models.CharField(max_length=255)),
                ('debris', models.CharField(max_length=255)),
                ('comments', models.TextField(null=True)),
                ('tape_Down', models.DecimalField(max_digits=6, decimal_places=3)),
                ('stage', models.DecimalField(max_digits=6, decimal_places=3)),
            ],
        ),
    ]
