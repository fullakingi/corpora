# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-13 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0048_group_duration'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='group',
            index=models.Index(fields=['-score'], name='people_grou_score_73dd1b_idx'),
        ),
        migrations.AddIndex(
            model_name='group',
            index=models.Index(fields=['num_recordings'], name='people_grou_num_rec_da0dc8_idx'),
        ),
        migrations.AddIndex(
            model_name='group',
            index=models.Index(fields=['duration'], name='people_grou_duratio_5a6d43_idx'),
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['-score'], name='people_pers_score_3f8d22_idx'),
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['score_comp'], name='people_pers_score_c_d8885e_idx'),
        ),
    ]
