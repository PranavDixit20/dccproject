# Generated by Django 2.0.5 on 2018-05-09 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0012_auto_20180509_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='callallocate',
            name='engg_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
