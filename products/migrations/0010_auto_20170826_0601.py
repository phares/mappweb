# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-26 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20170825_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='type',
            field=models.CharField(choices=[('DRINK', 'drink'), ('VEGETABLE', 'vegetable')], max_length=100),
        ),
    ]
