# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-26 23:35
from __future__ import unicode_literals

import corpus.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0027_auto_20180223_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='recording',
            name='audio_file_wav',
            field=models.FileField(blank=True, null=True, upload_to=corpus.models.upload_directory),
        ),
    ]