# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-25 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(upload_to='categories'),
        ),
    ]
