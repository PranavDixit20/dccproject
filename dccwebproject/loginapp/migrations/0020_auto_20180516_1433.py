# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-16 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0019_auto_20180516_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callallocate',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
