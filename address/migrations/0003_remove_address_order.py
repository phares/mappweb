# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 22:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_address_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='order',
        ),
    ]
