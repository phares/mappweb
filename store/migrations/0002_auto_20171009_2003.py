# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-09 20:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='name',
            field=models.CharField(default='Boby Wines', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='store_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transporter',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transporter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transporter',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='transport_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
