# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-08 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20171001_2335'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='orders.Order'),
            preserve_default=False,
        ),
    ]
