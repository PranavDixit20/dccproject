from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

class callallocate(models.Model):
    eng_name = models.CharField(max_length=100)
    comp_name = models.CharField(max_length=200)
    comp_address = models.TextField()
    comp_email = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    comp_problem = models.TextField()
    call_alloc = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

class coadmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    co_name = models.CharField(max_length=200)
    co_address = models.TextField()
    co_email = models.EmailField(max_length=70)
    phone_coregex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact_number = models.CharField(validators=[phone_coregex], max_length=17, blank=True)
    tell_no = models.CharField(max_length=17,blank=True)
    co_city = models.CharField(max_length=70)
    branch_code = models.CharField(max_length=100)
    co_gender = models.CharField(max_length=6)
    co_bdate = models.DateField(null=True, blank=True)
    co_age = models.IntegerField(null=True, blank=True)
    co_joining_date = models.DateField(null=True, blank=True)
    co_qual = models.CharField(max_length=50)
    co_designation = models.CharField(max_length=50)
    co_pass = models.CharField(max_length=16)
    co_conf_pass = models.CharField(max_length=16)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
     coadmin.objects.create(user=instance)
    instance.coadmin.save()
