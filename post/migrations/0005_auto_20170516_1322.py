# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20170516_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='part',
            field=models.IntegerField(blank=True, choices=[(1, 'US'), (2, 'EU'), (3, 'CSI'), (4, 'REST')], default=None, null=True),
        ),
    ]
