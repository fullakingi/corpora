# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-15 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0059_auto_20190606_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recording',
            name='language',
            field=models.CharField(blank=True, choices=[(b'mi', 'Maori'), (b'haw', 'Hawaiian'), (b'smo', 'Samoan'), (b'rar', 'Cook Island Maori')], default=b'mi', help_text='Language for a particular recording', max_length=16, verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='language',
            field=models.CharField(choices=[(b'mi', 'Maori'), (b'haw', 'Hawaiian'), (b'smo', 'Samoan'), (b'rar', 'Cook Island Maori')], default=b'mi', max_length=16),
        ),
        migrations.AlterField(
            model_name='text',
            name='primary_language',
            field=models.CharField(choices=[(b'mi', 'Maori'), (b'haw', 'Hawaiian'), (b'smo', 'Samoan'), (b'rar', 'Cook Island Maori')], default=b'mi', max_length=16, verbose_name='primary language'),
        ),
        migrations.AlterField(
            model_name='text',
            name='secondary_language',
            field=models.CharField(blank=True, choices=[(b'mi', 'Maori'), (b'haw', 'Hawaiian'), (b'smo', 'Samoan'), (b'rar', 'Cook Island Maori')], max_length=16, null=True, verbose_name='secondary language'),
        ),
    ]