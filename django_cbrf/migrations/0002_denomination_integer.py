# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-09 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_cbrf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='denomination',
            field=models.IntegerField(default=1, verbose_name='denomination'),
        ),
    ]
