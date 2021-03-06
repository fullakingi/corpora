# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-02 09:30
from __future__ import unicode_literals

import corpus.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0009_recording_sentence_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='recording',
            name='duration',
            field=models.FloatField(blank=True, default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='recording',
            name='audio_file',
            field=models.FileField(upload_to=corpus.models.upload_directory),
        ),
    ]
