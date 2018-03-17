from django import forms
from django.core.validators import RegexValidator

class RegisterForm(forms.Form):
    coadmin_id = forms.IntegerField()
    coadmin_name = forms.CharField(max_length=200)
    coadmin_address = forms.CharField(max_length=1000)
    coadmin_email = forms.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    coadmin_number = forms.CharField(validators=[phone_regex], max_length=1)
    coadmin_telephone = forms.CharField(max_length=12)
    coadmin_city = forms.CharField(max_length=70)
    coadmin_branch_code = forms.CharField(max_length=100)
    coadmin_gender = forms.CharField(max_length=6)
    coadmin_bdate = forms.DateField()
    coadmin_age = forms.IntegerField()
    coadmin_joining_date = forms.DateField()
    coadmin_qualification = forms.CharField(max_length=50)
    coadmin_designation = forms.CharField(max_length=50)
    coadmin_photo = forms.ImageField()
    coadmin_password = forms.CharField(max_length=16)
    coadmin_conf_pass = forms.CharField(max_length=16)
