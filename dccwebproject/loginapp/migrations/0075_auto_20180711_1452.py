# Generated by Django 2.0.6 on 2018-07-11 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0074_remove_callallocate_engg_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='callallocate',
            name='engg_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='loginapp.engg'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='engg',
            name='engg_skill',
            field=models.CharField(blank=True, choices=[('Online', 'Online'), ('Offline', 'Offline')], default=1, max_length=20, null=True),
        ),
    ]
