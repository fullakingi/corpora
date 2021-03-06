# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-09 04:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20180309_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageaction',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 9, 4, 12, 13, 957756, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messageaction',
            name='target_filter',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='messageaction',
            name='target_id',
            field=models.PositiveIntegerField(help_text='If target id is null, all objects of target will be acted on.', null=True),
        ),
        migrations.AlterField(
            model_name='messageaction',
            name='target_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
