# Generated by Django 2.0.5 on 2018-06-04 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0042_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='callallocate',
            name='client_sign_pic',
            field=models.ImageField(blank=True, null=True, upload_to='loginapp.ConsolePicture/bytes/filename/mimetype'),
        ),
        migrations.AddField(
            model_name='callallocate',
            name='engg_bus_end',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='callallocate',
            name='engg_bus_start',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='callallocate',
            name='engg_client_pic',
            field=models.ImageField(blank=True, null=True, upload_to='loginapp.ConsolePicture/bytes/filename/mimetype'),
        ),
        migrations.AddField(
            model_name='callallocate',
            name='engg_complaint_note',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='callallocate',
            name='engg_end_reading',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='callallocate',
            name='engg_lat',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='callallocate',
            name='engg_long',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='callallocate',
            name='engg_part_pic',
            field=models.ImageField(blank=True, null=True, upload_to='loginapp.ConsolePicture/bytes/filename/mimetype'),
        ),
        migrations.AddField(
            model_name='callallocate',
            name='engg_rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='callallocate',
            name='engg_start_reading',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='callallocate',
            name='engg_ticket_amnt',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='callallocate',
            name='engg_ticket_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='callallocate',
            name='engg_total_distance',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='callallocate',
            name='engg_transport_type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]