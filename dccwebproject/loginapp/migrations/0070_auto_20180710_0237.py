# Generated by Django 2.0.6 on 2018-07-09 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0069_auto_20180709_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callallocate',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
