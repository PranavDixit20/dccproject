# Generated by Django 2.0.5 on 2018-06-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0052_auto_20180618_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callallocate',
            name='engg_solve',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
