# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-26 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='contact',
            field=models.CharField(default='', max_length=15),
        ),
    ]