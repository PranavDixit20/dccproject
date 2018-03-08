from django.db import models
from django.core.validators import RegexValidator

class callallocate(models.Model):
    eng_name = models.CharField(max_length=100)
    co_name = models.CharField(max_length=200)
    co_address = models.TextField()
    co_email = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    co_problem = models.TextField()
    call_alloc = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
