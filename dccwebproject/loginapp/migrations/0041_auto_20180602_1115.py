# Generated by Django 2.0.5 on 2018-06-02 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0040_auto_20180602_1111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='callallocate',
            old_name='call_prioriy',
            new_name='call_priority',
        ),
    ]