# Generated by Django 2.0.4 on 2018-05-06 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0008_auto_20180506_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callallocate',
            name='call_closed_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
