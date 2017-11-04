# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-09 21:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20171009_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(default='No Name', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='transporter',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transporters', to='store.Store'),
        ),
    ]