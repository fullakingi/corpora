# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-12 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_auto_20171112_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='license',
            field=models.TextField(help_text='The actual license text.', null=True),
        ),
    ]
