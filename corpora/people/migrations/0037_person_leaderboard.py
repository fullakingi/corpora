# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-22 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0036_person_receive_weekly_updates'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='leaderboard',
            field=models.BooleanField(default=True, help_text='Check to show your progress on the leaderboard.', verbose_name='Show me on the leaderboard'),
        ),
    ]
