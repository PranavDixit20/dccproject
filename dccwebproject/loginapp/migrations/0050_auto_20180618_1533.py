# Generated by Django 2.0.5 on 2018-06-18 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0049_auto_20180613_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='callallocate',
            old_name='engg_ticket_no',
            new_name='engg_solve',
        ),
    ]