# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-19 07:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0006_auto_20170919_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualitycontrol',
            name='approved_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
