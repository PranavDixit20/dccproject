from django.db import models
import json
from datetime import datetime
from django.db.models import Sum
from loginapp.choices import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.urls import reverse
from django.http import HttpResponseRedirect



class Visitor(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    session_key = models.CharField(max_length=40,null=True, blank=True)


class callallocate(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    complaint_no = models.IntegerField(null=True,blank=True)
    comp_address = models.TextField(null=True,blank=True)
    comp_email = models.CharField(max_length=200,null=True,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    description = models.TextField(null=True,blank=True)
    start = models.DateField(null=True,blank=True)
    call_alloc_time = models.TimeField(null=True,blank=True)
    engg_contact = models.CharField(validators=[phone_regex], max_length=17,null=True,blank=True)
    call_status = models.CharField(choices=CALL_CHOICES, default="Open",max_length=7,null=True,blank=True)
    call_type = models.CharField(choices=CALL_TYPE_CHOICES, default="Hardware",max_length=15,null=True,blank=True)
    cust_city = models.CharField(max_length=20,null=True,blank=True)
    end = models.DateField(null=True,blank=True)
    call_tat = models.IntegerField(null=True,blank=True)
    call_note = models.CharField(max_length=100,null=True,blank=True)
    product = models.CharField(max_length=100,null=True,blank=True)
    call_priority = models.CharField(choices=PRIORITY_CHOICES, default="High",max_length=7,null=True,blank=True)
    caller_name = models.CharField(max_length=50,null=True,blank=True)
    engg_name = models.CharField(max_length=7,null=True,blank=True)
    engg_id = models.IntegerField(null=True,blank=True)
    engg_status = models.CharField(choices=ENGG_CHOICES,default="Engineer Assign",max_length=100,null=True,blank=True)
    engg_lat = models.DecimalField(max_digits=20, decimal_places=4,null=True,blank=True)
    engg_long = models.DecimalField(max_digits=20, decimal_places=4,null=True,blank=True)
    engg_rating = models.CharField(max_length=10,null=True,blank=True)
    engg_part_pic = models.ImageField(upload_to='co_pic/',null=True,blank=True)
    engg_client_pic = models.ImageField(upload_to='co_pic/',null=True,blank=True)
    client_sign_pic = models.ImageField(upload_to='co_pic',null=True,blank=True)
    engg_complaint_note = models.CharField(max_length=100,null=True,blank=True)
    engg_transport_type = models.CharField(max_length=10,null=True,blank=True)
    engg_start_reading = models.CharField(max_length=10,null=True,blank=True)
    engg_end_reading = models.CharField(max_length=10,null=True,blank=True)
    engg_solve = models.CharField(max_length=100,null=True,blank=True)
    engg_ticket_amnt = models.CharField(max_length=10,null=True,blank=True)
    engg_total_distance = models.CharField(max_length=10,null=True,blank=True)
    engg_bus_start = models.CharField(max_length=10,null=True,blank=True)
    engg_bus_end = models.CharField(max_length=10,null=True,blank=True)
    engg_bike_no = models.CharField(max_length=10,null=True,blank=True)
    engg_part_name = models.CharField(max_length=10,null=True,blank=True)
    engg_part_no = models.CharField(max_length=30,null=True,blank=True)
    engg_feedback = models.CharField(max_length=200,null=True,blank=True)
    comp_rating = models.CharField(max_length=10,null=True,blank=True)
    comp_feedback = models.CharField(max_length=200,null=True,blank=True)



class coadmin(models.Model):
    co_name = models.CharField(max_length=200,null=True,blank=True)
    co_address = models.TextField(null=True,blank=True)
    co_email = models.EmailField(max_length=70,null=True,blank=True)
    phone_coregex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact_number = models.CharField(validators=[phone_coregex], max_length=17, blank=True)
    tell_no = models.CharField(max_length=17,null=True,blank=True)
    co_city = models.CharField(max_length=70,null=True,blank=True)
    branch_code = models.CharField(max_length=100,null=True,blank=True)
    co_gender = models.CharField(choices=GENDER_CHOICES, default=1, max_length=6,null=True,blank=True)
    co_bdate = models.DateTimeField(null=True,blank=True)
    co_age = models.IntegerField(null=True, blank=True)
    co_joining_date = models.DateTimeField(null=True,blank=True)
    co_qual = models.CharField(max_length=50,null=True,blank=True)
    co_designation = models.CharField(max_length=50,null=True,blank=True)
    co_pass = models.CharField(max_length=16,null=True,blank=True)
    co_conf_pass = models.CharField(max_length=16,null=True,blank=True)

    def get_absolute_url(self):
        return reverse("loginapp:coregister", kwargs={'pk':self.pk})



class customer(models.Model):
    customer_name = models.CharField(max_length=100,null=True,blank=True)
    customer_area = models.CharField(max_length=500,null=True,blank=True)
    customer_landmark = models.CharField(max_length=500,null=True,blank=True)
    customer_city = models.CharField(max_length=500,null=True,blank=True)
    customer_pincode = models.IntegerField(null=True,blank=True)
    cutomer_fax = models.CharField(max_length=11,null=True,blank=True)
    customer_compay_type = models.CharField(max_length=50,null=True,blank=True)
    customer_doc = models.DateField(null=True,blank=True)
    customer_email = models.EmailField(null=True,blank=True)
    phone_curegex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    customer_contact_no = models.CharField(validators=[phone_curegex],max_length=17,null=True,blank=True)
    customer_agreement = models.IntegerField(null=True,blank=True)
    customer_agreement_amount = models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    gstin_curegex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="GSTIN number must be entered in the format: '999999999'. Up to 15 digits allowed.")
    customer_GSTIN_no = models.CharField(validators=[gstin_curegex],max_length=20,null=True,blank=True)
    customer_product = models.CharField(max_length=50,null=True,blank=True)


    def __str__(self):
        return self.customer_name



class engg(models.Model):
    engg_id = models.IntegerField(null=True,blank=True)
    engg_pic = models.ImageField(upload_to='co_pic/',null=True,blank=True)
    engg_name = models.CharField(max_length=200,null=True,blank=True)
    engg_address = models.TextField(null=True,blank=True)
    engg_permanent_address=models.TextField(null=True,blank=True)
    engg_email = models.EmailField(max_length=70,null=True,blank=True)
    engg_phone_coregex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    engg_contact_number = models.CharField(validators=[engg_phone_coregex], max_length=17, blank=True)
    engg_tell_no = models.CharField(max_length=17,blank=True)
    engg_city = models.CharField(max_length=70, null=True, blank=True)
    engg_branch_code = models.CharField(max_length=100,null=True,blank=True)
    engg_gender = models.CharField(choices=GENDER_CHOICES, default=1,max_length=12,null=True,blank=True)
    engg_bdate = models.DateField(null=True,blank=True)
    engg_age = models.IntegerField(null=True, blank=True)
    engg_joining_date = models.DateField(null=True,blank=True)
    engg_qual = models.CharField(max_length=50,null=True,blank=True)
    engg_designation = models.CharField(max_length=50,null=True,blank=True)
    engg_skill=models.CharField(max_length=20,null=True,blank=True)
    engg_pass = models.CharField(max_length=16,null=True,blank=True)
    engg_conf_pass = models.CharField(max_length=16,null=True,blank=True)
    engg_status = models.CharField(choices=STATUS_CHOICES, default=1,max_length=12,null=True,blank=True)

    def __str__(self):
        return self.engg_name

    def save(self, *args, **kwargs):
        #delete_file_if_needed(self, 'picture')
        super(engg, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(engg, self).delete(*args, **kwargs)
        delete_file(self, 'picture')


class enggperformance(models.Model):
    engg_id = models.IntegerField(null=True,blank=True)
    calls_closed = models.IntegerField(null=True,blank=True)
    avg_rating = models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    mode_of_transport = models.CharField(max_length=20,null=True,blank=True)
    total_distance_travelled = models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    tickets = models.FileField(null=True,blank=True)
    total_ticket_amnt = models.IntegerField(null=True,blank=True)
    battery_percentage = models.IntegerField(null=True,blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=4,null=True,blank=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=4,null=True,blank=True)
    punchin_time = models.TimeField(null=True,blank=True)
    punchout_time = models.TimeField(null=True,blank=True)
    online_status = models.BooleanField()



class stock(models.Model):
    product_name = models.CharField(max_length=20,null=True,blank=True)
    product_size = models.CharField(max_length=20,null=True,blank=True)
    product_quantity = models.IntegerField(null=True,blank=True)
    product_code = models.IntegerField(null=True,blank=True)
    product_recieved_date = models.DateField(null=True,blank=True)
    product_provider_name = models.CharField(max_length=20,null=True,blank=True)
    Total_product_quantity = models.IntegerField(null=True,blank=True)
    product_serial_no = models.IntegerField(null=True,blank=True)
    product_model = models.CharField(max_length=20,null=True,blank=True)
    product_model_id = models.IntegerField(null=True,blank=True)
    product_description = models.CharField(max_length=500,null=True,blank=True)
    product_warranty = models.IntegerField(null=True,blank=True)
    #stock.objects.aggregate(Sum('product_quantity'))

class products(models.Model):
    product_name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.product_name
