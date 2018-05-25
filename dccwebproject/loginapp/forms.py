from django import forms
from django.forms import ModelChoiceField
from loginapp.choices import *
from . import views
from . models import engg,stock
from django.contrib.admin import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



class RegisterForm(forms.Form):
  name = forms.CharField(max_length=20)
  email = forms.EmailField(required=True)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
  mobile_number = forms.CharField(validators=[phone_regex], max_length=17)
  telephone_number = forms.CharField(validators=[phone_regex], max_length=17)
  city = forms.CharField(max_length=10)
  branch_code = forms.IntegerField(required=True)
  gender = forms.ChoiceField(choices = GENDER_CHOICES, label="gender", initial='M', widget=forms.Select())
  birth_date = forms.DateField()
  age = forms.IntegerField()
  joining_date = forms.DateField()
  qualification = forms.CharField(max_length=10)
  designation = forms.CharField(max_length=10)
  password = forms.CharField(widget=forms.PasswordInput)
  confirm_password = forms.CharField(widget=forms.PasswordInput)
  address = forms.CharField(max_length=100,widget=forms.Textarea)


class EnggRegisterForm(forms.Form):
  engg_id = forms.IntegerField(required=True)
  engg_photo = forms.FileField()
  name = forms.CharField(max_length=20)
  email = forms.EmailField(required=True)
  address = forms.CharField(max_length=100,widget=forms.Textarea)
  permanent_address = forms.CharField(max_length=100,widget=forms.Textarea)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
  mobile_number = forms.CharField(validators=[phone_regex], max_length=17)
  telephone_number = forms.CharField(validators=[phone_regex], max_length=17)
  city = forms.CharField(max_length=10)
  branch_code = forms.IntegerField(required=True)
  gender = forms.ChoiceField(choices = GENDER_CHOICES, label="gender", initial='M', widget=forms.Select())
  birth_date = forms.DateField()
  age = forms.IntegerField()
  joining_date = forms.DateField()
  qualification = forms.CharField(max_length=10)
  designation = forms.CharField(max_length=10)
  skills = forms.CharField(max_length = 20)
  password = forms.CharField(widget=forms.PasswordInput)
  confirm_password = forms.CharField(widget=forms.PasswordInput)
  status = forms.ChoiceField(choices = STATUS_CHOICES, label="status", initial='Offline', widget=forms.Select())

class CustomerRegisterForm(forms.Form):
   name = forms.CharField(max_length=100)
   area = forms.CharField(max_length=500)
   landmark = forms.CharField(max_length=500)
   city = forms.CharField(max_length=500)
   pincode = forms.IntegerField()
   fax_no = forms.CharField(max_length=11)
   company_Type = forms.CharField(max_length=50)
   date_of_creation = forms.DateField()
   email = forms.EmailField()
   phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
   contact_number = forms.CharField(validators=[phone_regex], max_length=17)
   customer_agreement = forms.IntegerField()
   agreement_amount = forms.DecimalField(max_digits=20, decimal_places=2)
   product1 = forms.CharField(max_length=50)
   product2 = forms.CharField(max_length=50)
   product3 = forms.CharField(max_length=50)
   product4 = forms.CharField(max_length=50)

class CallAllocateForm(forms.Form):
    company_name = forms.CharField(max_length=200)
    company_address = forms.CharField(max_length=100,widget=forms.Textarea)
    company_email = forms.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact_number = forms.CharField(validators=[phone_regex], max_length=17)
    company_problem = forms.CharField(max_length=100,widget=forms.Textarea)
    call_allocation_date =  forms.DateField()
    call_allocation_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    engg_name = forms.CharField(max_length=100)
    engg_id = forms.IntegerField()
    engg_contact = forms.CharField(validators=[phone_regex], max_length=17)
    engg_status = forms.ChoiceField(choices = ENGG_CHOICES, label="engg status", initial='O', widget=forms.Select())
    call_status = forms.ChoiceField(choices = CALL_CHOICES, label="call status", initial='O', widget=forms.Select())
    call_type = forms.CharField(max_length=7)
    company_city = forms.CharField(max_length=20)
    call_auto_close_date = forms.DateField()
    call_TAT = forms.IntegerField()
    call_note = forms.CharField(max_length=100)
    product = forms.CharField(max_length=100)
    call_priority = forms.CharField(max_length=7)
    caller_name = forms.CharField(max_length=50)

class StockEntry(forms.ModelForm):
    class Meta:
        model = stock
        fields = '__all__'
