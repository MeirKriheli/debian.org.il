# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Added at'),
        ),
    ]