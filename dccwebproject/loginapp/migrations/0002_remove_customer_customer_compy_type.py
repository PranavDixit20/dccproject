# Generated by Django 2.0.4 on 2018-04-16 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customer_compy_type',
        ),
    ]
