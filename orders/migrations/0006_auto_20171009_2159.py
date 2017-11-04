# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-09 21:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20171009_2159'),
        ('orders', '0005_auto_20171008_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='store',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='store', to='store.Store'),
        ),
        migrations.AddField(
            model_name='order',
            name='transporter',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transporter', to='store.Transporter'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('CANCELLED', 'CANCELLED'), ('COMPLETED', 'COMPLETED'), ('PROCESSING', 'PROCESSING'), ('FAILED', 'FAILED'), ('RECEIVED', 'RECEIVED')], default='RECEIVED', max_length=20),
        ),
    ]