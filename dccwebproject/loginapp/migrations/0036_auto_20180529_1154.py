# Generated by Django 2.0.5 on 2018-05-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0035_auto_20180529_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callallocate',
            name='call_type',
            field=models.CharField(blank=True, choices=[('Hardware', 'Hardware'), ('Networking', 'Networking'), ('Software', 'Software')], default='Hardware', max_length=15, null=True),
        ),
    ]