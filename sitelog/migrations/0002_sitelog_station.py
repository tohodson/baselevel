# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitelog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitelog',
            name='station',
            field=models.IntegerField(default=104),
            preserve_default=False,
        ),
    ]