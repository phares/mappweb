# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='type',
            field=models.CharField(choices=[('DRINKS', 'drink'), ('VEGETABLES', 'vegetable'), ('FRUITS', 'fruit')], default='drink', max_length=100),
        ),
    ]
