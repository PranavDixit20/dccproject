# Generated by Django 2.0.4 on 2018-04-13 07:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='callallocate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_name', models.CharField(blank=True, max_length=100, null=True)),
                ('comp_name', models.CharField(blank=True, max_length=200, null=True)),
                ('comp_address', models.TextField(blank=True, null=True)),
                ('comp_email', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('comp_problem', models.TextField(blank=True, null=True)),
                ('call_alloc_date', models.DateTimeField(blank=True, null=True)),
                ('call_alloc_time', models.TimeField(blank=True, null=True)),
                ('call_alloc_engg_name', models.CharField(blank=True, max_length=20, null=True)),
                ('engg_contact', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('call_status', models.CharField(blank=True, max_length=7, null=True)),
                ('call_closed_date', models.DateField(blank=True, null=True)),
                ('engg_longitude', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('engg_latitude', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('call_type', models.CharField(blank=True, max_length=7, null=True)),
                ('cust_ratings', models.IntegerField(blank=True, null=True)),
                ('cust_city', models.CharField(blank=True, max_length=20, null=True)),
                ('call_auto_close_date', models.DateField(blank=True, null=True)),
                ('call_tat', models.IntegerField(blank=True, null=True)),
                ('call_note', models.CharField(blank=True, max_length=100, null=True)),
                ('complaint_no', models.IntegerField(blank=True, null=True)),
                ('call_images_uploaded', models.ImageField(blank=True, null=True, upload_to='co_pic/')),
                ('part_pickup_date', models.DateField(blank=True, null=True)),
                ('part_delivery_date', models.DateField(blank=True, null=True)),
                ('part_name', models.CharField(blank=True, max_length=100, null=True)),
                ('part_warranty', models.IntegerField(blank=True, null=True)),
                ('product', models.CharField(blank=True, max_length=100, null=True)),
                ('call_prioriy', models.CharField(blank=True, max_length=7, null=True)),
                ('engg_call_start_time', models.TimeField(blank=True, null=True)),
                ('engg_call_end_time', models.TimeField(blank=True, null=True)),
                ('engg_job_start_time', models.TimeField(blank=True, null=True)),
                ('engg_job_end_time', models.TimeField(blank=True, null=True)),
                ('engg_probelm_solve_msg', models.TextField(blank=True, null=True)),
                ('engg_rating', models.IntegerField(blank=True, null=True)),
                ('engg_feedback', models.TextField(blank=True, null=True)),
                ('engg_status', models.CharField(blank=True, max_length=30, null=True)),
                ('caller_name', models.CharField(blank=True, max_length=50, null=True)),
                ('engg_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='coadmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_name', models.CharField(blank=True, max_length=200, null=True)),
                ('co_address', models.TextField(blank=True, null=True)),
                ('co_email', models.EmailField(blank=True, max_length=70, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('tell_no', models.CharField(blank=True, max_length=17, null=True)),
                ('co_city', models.CharField(blank=True, max_length=70, null=True)),
                ('branch_code', models.CharField(blank=True, max_length=100, null=True)),
                ('co_gender', models.CharField(blank=True, max_length=6, null=True)),
                ('co_bdate', models.DateTimeField(blank=True, null=True)),
                ('co_age', models.IntegerField(blank=True, null=True)),
                ('co_joining_date', models.DateTimeField(blank=True, null=True)),
                ('co_qual', models.CharField(blank=True, max_length=50, null=True)),
                ('co_designation', models.CharField(blank=True, max_length=50, null=True)),
                ('co_pass', models.CharField(blank=True, max_length=16, null=True)),
                ('co_conf_pass', models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_area', models.CharField(blank=True, max_length=500, null=True)),
                ('customer_landmark', models.CharField(blank=True, max_length=500, null=True)),
                ('customer_city', models.CharField(blank=True, max_length=500, null=True)),
                ('customer_pincode', models.IntegerField(blank=True, null=True)),
                ('cutomer_fax', models.CharField(blank=True, max_length=11, null=True)),
                ('customer_compay_type', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_doc', models.DateTimeField(blank=True, null=True)),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('customer_contact_no', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('customer_compy_type', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_agreement', models.IntegerField(blank=True, null=True)),
                ('customer_agreement_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('customer_product1', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_product2', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_product3', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_product4', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='engg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engg_id', models.IntegerField(blank=True, null=True)),
                ('engg_name', models.CharField(blank=True, max_length=200, null=True)),
                ('engg_address', models.TextField(blank=True, null=True)),
                ('engg_permanent_address', models.TextField(blank=True, null=True)),
                ('engg_email', models.EmailField(blank=True, max_length=70, null=True)),
                ('engg_contact_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('engg_tell_no', models.CharField(blank=True, max_length=17)),
                ('engg_city', models.CharField(blank=True, max_length=70, null=True)),
                ('engg_branch_code', models.CharField(blank=True, max_length=100, null=True)),
                ('engg_gender', models.CharField(blank=True, max_length=12, null=True)),
                ('engg_bdate', models.DateTimeField(blank=True, null=True)),
                ('engg_age', models.IntegerField(blank=True, null=True)),
                ('engg_joining_date', models.DateTimeField(blank=True, null=True)),
                ('engg_qual', models.CharField(blank=True, max_length=50, null=True)),
                ('engg_designation', models.CharField(blank=True, max_length=50, null=True)),
                ('engg_skill', models.CharField(blank=True, max_length=20, null=True)),
                ('engg_pass', models.CharField(blank=True, max_length=16, null=True)),
                ('engg_conf_pass', models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
    ]