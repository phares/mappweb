# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-08 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20171001_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('CANCELLED', 'CANCELLED'), ('COMPLETED', 'COMPLETED'), ('PROCESSING', 'PROCESSING'), ('FAILED', 'FAILED'), ('RECEIVED', 'RECEIVED')], default='Active', max_length=20),
        ),
    ]
