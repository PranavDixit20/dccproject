# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-16 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0020_auto_20180516_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callallocate',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]