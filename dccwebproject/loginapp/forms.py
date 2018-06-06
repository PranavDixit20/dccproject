from django import forms
from django.forms import ModelChoiceField
from loginapp.choices import *
from . import views
from . models import engg,stock,callallocate,customer
from django.contrib.admin import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from db_file_storage.form_widgets import DBClearableFileInput



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


class EnggRegisterForm(forms.ModelForm):
    class Meta:
        model = engg
        exclude = []
        fields = '__all__'
        widgets = {
            'engg_pic': DBClearableFileInput,
            'engg_bdate':forms.DateInput(attrs={'type':'date'}),
        }

class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = customer
        exclude = []
        fields = '__all__'
        product1=forms.ChoiceField(choices=PRODUCT_CHOICES)



def getaddr(request):
    addr = customer.objects.filter(customer_name=request.session.get('city')).values_list('customer_city')
    return addr

class CallAllocateForm(forms.ModelForm):
    qset = customer.objects.all()
    #eqset = engg.objects.filter(engg_city=)
    title = forms.ModelChoiceField(queryset=qset)
    #engg_name = forms.ModelChoiceField(queryset=eqset)

    class Meta:
        model = callallocate
        exclude = [
        'complaint_no',
        'engg_lat',
        'engg_long',
        'engg_rating',
        'engg_part_pic',
        'engg_client_pic',
        'client_sign_pic',
        'engg_complaint_note',
        'engg_transport_type',
        'engg_start_reading',
        'engg_end_reading',
        'engg_ticket_no',
        'engg_ticket_amnt',
        'engg_total_distance',
        'engg_bus_start',
        'engg_bus_end'
        ]
        fields = '__all__'
        widgets = {
            'call_alloc_time':forms.TimeInput(attrs={'type':'time'}),
            'start':forms.DateInput(attrs={'type':'date'}),
            'end':forms.TimeInput(attrs={'type':'date'}),
        }

class StockEntry(forms.ModelForm):
    class Meta:
        model = stock
        fields = '__all__'
