from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import json
from loginapp.pswdgen import *
from datetime import datetime
from loginapp.choices import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.urls import reverse
from django.http import HttpResponseRedirect


# class Message(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
#     message = models.CharField(max_length=1200)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     is_read = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.message
#
#     class Meta:
#         ordering = ('timestamp',)
#
# class Visitor(models.Model):
#     user = models.OneToOneField(User,on_delete = models.CASCADE)
#     session_key = models.CharField(max_length=40,null=True, blank=True)

class Customer(models.Model):
    # user = models.OneToOneField(User,on_delete = models.CASCADE)
    customer_name = models.CharField(max_length=500,null=True,blank=False)
    customer_adrress = models.CharField(max_length=500,null=True,blank=False)
    customer_city = models.CharField(max_length=500,null=True,blank=True)
    customer_pincode = models.IntegerField(null=True,blank=True)
    cutomer_fax = models.CharField(max_length=11,null=True,blank=True)
    customer_company_type = models.CharField(max_length=50,null=True,blank=True)
    customer_doc = models.DateField(auto_now_add=True)
    customer_email = models.EmailField(null=True,blank=False)
    phone_curegex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    customer_contact_no = models.CharField(validators=[phone_curegex],max_length=17,null=True,blank=True)
    customer_agreement_from = models.DateField(null=True,blank=False)
    customer_agreement_to = models.DateField(null=True,blank=False)
    customer_agreement_amount = models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    gstin_curegex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="GSTIN number must be entered in the format: '999999999'. Up to 15 digits allowed.")
    customer_GSTIN_no = models.CharField(validators=[gstin_curegex],max_length=20,null=True,blank=True)
    customer_product = models.CharField(max_length=40,null=True,blank=True)

    def __str__(self):
            return self.customer_name

# @receiver(post_save,sender=User)
# def update_customer_profile(sender,instance,created,**kwargs):
#     if created:
#         Customer.objects.create(user=instance)
#     instance.customer.save()


class engg(models.Model):
    pswd = passGen(8)
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    engg_id = models.CharField(max_length=10,null=True,blank=False,verbose_name=u"Engineer id *")
    engg_pic = models.ImageField(upload_to='co_pic/profile/',null=True,blank=False,verbose_name=u"Engineer photo *")
    engg_name = models.CharField(max_length=200,null=True,blank=False,verbose_name=u"Engineer Name *")
    engg_address = models.TextField(null=True,blank=False,verbose_name=u"Engineer Address")
    engg_permanent_address=models.TextField(null=True,blank=True,verbose_name=u"Engineer Permanent Address")
    engg_email = models.EmailField(max_length=70,null=True,blank=False,verbose_name=u"Engineer E-mail id")
    engg_phone_coregex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    engg_contact_number = models.CharField(validators=[engg_phone_coregex], max_length=17, blank=True,verbose_name=u"Engineer Contact Number")
    engg_tell_no = models.CharField(max_length=17,blank=True,verbose_name=u"Engineer Telephone Number")
    engg_city = models.CharField(max_length=70, null=True, blank=False,verbose_name=u"Engineer City")
    engg_branch_code = models.CharField(max_length=100,null=True,blank=False,verbose_name=u"Engineer Branch Code")
    engg_gender = models.CharField(choices=GENDER_CHOICES, default=1,max_length=12,null=True,blank=True,verbose_name=u"Engineer Gender")
    engg_bdate = models.DateField(null=True,blank=True,verbose_name=u"Engineer Birth Date")
    engg_age = models.IntegerField(null=True, blank=True,verbose_name=u"Engineer Age")
    engg_joining_date = models.DateField(null=True,blank=True,verbose_name=u"Engineer Joining Date")
    engg_qual = models.CharField(max_length=50,null=True,blank=True,verbose_name=u"Engineer Qualification")
    engg_designation = models.CharField(max_length=50,null=True,blank=True,verbose_name=u"Engineer Designation")
    engg_skill=models.CharField(choices=CALL_TYPE_CHOICES, default=1,max_length=20,null=True,blank=True,verbose_name=u"Engineer Skill")
    engg_pass = models.CharField(max_length=16,null=True,blank=False,default=pswd,verbose_name=u"Engineer Password")
    engg_conf_pass = models.CharField(max_length=16,null=True,blank=False,default=pswd,verbose_name=u"Engineer Confirm Password")
    engg_status = models.CharField(choices=STATUS_CHOICES, default=1,max_length=12,null=True,blank=True,verbose_name=u"Engineer Status")
    engg_lat = models.DecimalField(max_digits=20, decimal_places=4,null=True,blank=True)
    engg_long = models.DecimalField(max_digits=20, decimal_places=4,null=True,blank=True)
    battery_percentage = models.IntegerField(null=True,blank=True)
    complaint_id = models.CharField(max_length=200,null=True,blank=False)

    def __str__(self):
        return '%s %s' %(self.engg_id,self.engg_name)

# @receiver(post_save,sender=User)
# def update_user_engg(sender,instance,created,**kwargs):
#     if created:
#         engg.objects.create(user=instance)
#     instance.engg.save()



class callallocate(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True,blank=True)
    complaint_no = models.CharField(max_length=200,null=True,blank=True)
    comp_address = models.TextField(null=True,blank=True)
    comp_email = models.CharField(max_length=200,null=True,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    product = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    start = models.DateTimeField(auto_now_add=True,null=True,blank=False)
    engg_contact = models.CharField(validators=[phone_regex], max_length=17,null=True,blank=True)
    call_status = models.CharField(choices=CALL_CHOICES, default="Open",max_length=7,null=True,blank=True)
    call_type = models.CharField(choices=CALL_TYPE_CHOICES, default="Hardware",max_length=15,null=True,blank=True)
    cust_city = models.CharField(max_length=20,null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    call_tat = models.IntegerField(null=True,blank=True)
    call_note = models.CharField(max_length=100,null=True,blank=True)
    call_priority = models.CharField(choices=PRIORITY_CHOICES, default="High",max_length=7,null=True,blank=True)
    caller_name = models.CharField(max_length=50,null=True,blank=True)
    engg_id = models.ForeignKey(engg,on_delete=models.CASCADE)
    engineer_id = models.CharField(max_length=10,null=True,blank=True)
    engg_name = models.CharField(max_length=100,null=True,blank=True)
    engg_status = models.CharField(choices=ENGG_CHOICES,default="Engineer Assign",max_length=100,null=True,blank=True)
    engg_lat = models.DecimalField(max_digits=20, decimal_places=4,null=True,blank=True)
    engg_long = models.DecimalField(max_digits=20, decimal_places=4,null=True,blank=True)
    battery_percentage = models.IntegerField(null=True,blank=True)
    engg_rating = models.CharField(max_length=10,null=True,blank=True)
    engg_part_pic = models.ImageField(upload_to='co_pic/part/',null=True,blank=True)
    engg_client_pic = models.ImageField(upload_to='co_pic/',null=True,blank=True)
    client_sign_pic = models.ImageField(upload_to='co_pic/sign/',null=True,blank=True)
    engg_complaint_note = models.CharField(max_length=100,null=True,blank=True)
    engg_transport_type = models.CharField(max_length=10,null=True,blank=True)
    engg_start_reading = models.CharField(max_length=10,null=True,blank=True)
    engg_start_reading_pic = models.ImageField(upload_to='co_pic/',null=True,blank=True)
    engg_end_reading = models.CharField(max_length=10,null=True,blank=True)
    engg_end_reading_pic = models.ImageField(upload_to='co_pic/',null=True,blank=True)
    engg_solve = models.CharField(max_length=100,null=True,blank=True)
    engg_ticket_amnt = models.CharField(max_length=10,null=True,blank=True)
    engg_total_distance = models.CharField(max_length=10,null=True,blank=True)
    engg_bus_start = models.CharField(max_length=10,null=True,blank=True)
    engg_bus_end = models.CharField(max_length=10,null=True,blank=True)
    engg_bus_ticket_pic = models.ImageField(upload_to='co_pic/',null=True,blank=True)
    engg_bike_no = models.CharField(max_length=10,null=True,blank=True)
    engg_part_name = models.CharField(max_length=10,null=True,blank=True)
    engg_part_no = models.CharField(max_length=30,null=True,blank=True)
    engg_feedback = models.CharField(max_length=200,null=True,blank=True)
    comp_rating = models.CharField(max_length=10,null=True,blank=True)
    comp_feedback = models.CharField(max_length=200,null=True,blank=True)



class coadmin(models.Model):
    pswd = passGen(8)
    co_name = models.CharField(max_length=200,null=True,blank=False,verbose_name=u"Name")
    co_address = models.TextField(null=True,blank=True,verbose_name=u"Address")
    co_email = models.EmailField(max_length=70,null=True,blank=False,verbose_name=u"E-mail")
    phone_coregex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact_number = models.CharField(validators=[phone_coregex], max_length=17, blank=True,verbose_name=u"Contact Number")
    tell_no = models.CharField(max_length=17,null=True,blank=True,verbose_name=u"Telephone Number")
    co_city = models.CharField(max_length=70,null=True,blank=False,verbose_name=u"City")
    branch_code = models.CharField(max_length=100,null=True,blank=False,verbose_name=u"Branch Code")
    co_gender = models.CharField(choices=GENDER_CHOICES, default=1, max_length=6,null=True,blank=True,verbose_name=u"Gender")
    co_bdate = models.DateTimeField(null=True,blank=True,verbose_name=u"Birth Date")
    co_age = models.IntegerField(null=True, blank=True,verbose_name=u"Age")
    co_joining_date = models.DateTimeField(null=True,blank=True,verbose_name=u"Joining Date")
    co_qual = models.CharField(max_length=50,null=True,blank=True,verbose_name=u"Qualification")
    co_designation = models.CharField(max_length=50,null=True,blank=True,verbose_name=u"Designation")
    co_pass = models.CharField(max_length=16,null=True,blank=True,verbose_name=u"Password")
    co_conf_pass = models.CharField(max_length=16,null=True,blank=True,verbose_name=u"Confirm Password")
    co_status =  models.CharField(choices=STATUS_CHOICES, default='Offline',max_length=12,null=True,blank=True,verbose_name=u" Status")

    def get_absolute_url(self):
        return reverse("loginapp:coregister", kwargs={'pk':self.pk})


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
    product_name = models.CharField(max_length=20,null=True,blank=False)
    product_size = models.CharField(max_length=20,null=True,blank=False)
    product_quantity = models.IntegerField(null=True,blank=False)
    product_code = models.IntegerField(null=True,blank=False)
    product_recieved_date = models.DateField(null=True,blank=False)
    product_provider_name = models.CharField(max_length=20,null=True,blank=False)
    Total_product_quantity = models.IntegerField(null=True,blank=False)
    product_serial_no = models.IntegerField(null=True,blank=False)
    product_model = models.CharField(max_length=20,null=True,blank=False)
    product_model_id = models.IntegerField(null=True,blank=False)
    product_description = models.CharField(max_length=500,null=True,blank=True)
    product_warranty = models.IntegerField(null=True,blank=False)


class products(models.Model):
    product_name = models.CharField(max_length=100,null=True,blank=False)
    def __str__(self):
         return self.product_name

class performance(models.Model):
    r_id = models.ForeignKey(engg,on_delete=models.CASCADE)
    total_open = models.IntegerField(null=True,blank=True)
    total_closed = models.IntegerField(null=True,blank=True)
    total_pending = models.IntegerField(null=True,blank=True)
    stars = models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
