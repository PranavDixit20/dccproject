# Generated by Django 2.0.4 on 2018-04-29 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0005_auto_20180421_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coadmin',
            name='co_gender',
            field=models.CharField(blank=True, choices=[(1, 'Male'), (2, 'Female')], default=1, max_length=6, null=True),
        ),
    ]