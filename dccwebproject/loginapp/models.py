from django.db import models
from datetime import datetime
from loginapp.choices import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.urls import reverse
from django.http import HttpResponseRedirect


class callallocate(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    comp_address = models.TextField(null=True,blank=True)
    comp_email = models.CharField(max_length=200,null=True,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    description = models.TextField(null=True,blank=True)
    start = models.DateTimeField(auto_now_add=True, editable=False,null=True,blank=True)
    call_alloc_time = models.TimeField(null=True,blank=True)
    engg_contact = models.CharField(validators=[phone_regex], max_length=17,null=True,blank=True)
    call_status = models.CharField(choices=GENDER_CHOICES, default=1,max_length=7,null=True,blank=True)
    call_type = models.CharField(max_length=7,null=True,blank=True)
    cust_city = models.CharField(max_length=20,null=True,blank=True)
    end = models.DateField(null=True,blank=True)
    call_tat = models.IntegerField(null=True,blank=True)
    call_note = models.CharField(max_length=100,null=True,blank=True)
    complaint_no = models.IntegerField(null=True,blank=True)
    product = models.CharField(max_length=100,null=True,blank=True)
    call_prioriy = models.CharField(max_length=7,null=True,blank=True)
    caller_name = models.CharField(max_length=50,null=True,blank=True)
    engg_name = models.CharField(max_length=100,null=True,blank=True)
    engg_id = models.IntegerField(null=True,blank=True)


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
    customer_doc = models.DateTimeField(null=True,blank=True)
    customer_email = models.EmailField(null=True,blank=True)
    phone_curegex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    customer_contact_no = models.CharField(validators=[phone_curegex],max_length=17,null=True,blank=True)
    customer_agreement = models.IntegerField(null=True,blank=True)
    customer_agreement_amount = models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    customer_product1 = models.CharField(max_length=50,null=True,blank=True)
    customer_product2 = models.CharField(max_length=50,null=True,blank=True)
    customer_product3 = models.CharField(max_length=50,null=True,blank=True)
    customer_product4 = models.CharField(max_length=50,null=True,blank=True)



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
    engg_city = models.CharField(max_length=70,null=True,blank=True)
    engg_branch_code = models.CharField(max_length=100,null=True,blank=True)
    engg_gender = models.CharField(choices=GENDER_CHOICES, default=1,max_length=12,null=True,blank=True)
    engg_bdate = models.DateTimeField(null=True,blank=True)
    engg_age = models.IntegerField(null=True, blank=True)
    engg_joining_date = models.DateTimeField(null=True,blank=True)
    engg_qual = models.CharField(max_length=50,null=True,blank=True)
    engg_designation = models.CharField(max_length=50,null=True,blank=True)
    engg_skill=models.CharField(max_length=20,null=True,blank=True)
    engg_pass = models.CharField(max_length=16,null=True,blank=True)
    engg_conf_pass = models.CharField(max_length=16,null=True,blank=True)


class enggperformance(models.Model):
    engg_id = models.ForeignKey(engg, on_delete = models.CASCADE)
    calls_closed = models.IntegerField(null=True,blank=True)
    avg_rating = models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    mode_of_transport = models.CharField(max_length=20,null=True,blank=True)
    total_distance_travelled = models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    tickets = models.FileField(null=True,blank=True)
    total_ticket_amnt = models.IntegerField(null=True,blank=True)
    battery_percentage = models.IntegerField(null=True,blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    punchin_time = models.TimeField(null=True,blank=True)
    punchout_time = models.TimeField(null=True,blank=True)
    online_status = models.BooleanField()
