from django import forms
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from . models import engg, stock, callallocate, Customer, products, coadmin
from django.contrib.admin import widgets
import datetime
import random







class RegisterForm(forms.ModelForm):
  class Meta:
      model = coadmin
      fields = "__all__"
      widgets = {
          'co_bdate':forms.DateInput(attrs={'type':'date'}),
          'co_joining_date':forms.DateInput(attrs={'type':'date'}),

      }



class EnggRegisterForm(forms.ModelForm):
    class Meta:
        model = engg
        exclude = [
        'engg_lat',
        'engg_long',
        'complaint_id',
        'battery_percentage',
        ]
        fields = '__all__'
        widgets = {

            'engg_bdate':forms.DateInput(attrs={'type':'date'}),
            'engg_joining_date':forms.DateInput(attrs={'type':'date'}),

        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class CustomerRegisterForm(forms.ModelForm):
    q = products.objects.all()
    customer_product = forms.ModelChoiceField(queryset=q)
    class Meta:
        model = Customer
        fields = ('customer_name','customer_email','customer_adrress',
        'customer_city','customer_pincode','customer_product',
        'customer_agreement_from','customer_agreement_to',
        'customer_agreement_amount','cutomer_fax','customer_company_type','customer_contact_no',
        'customer_GSTIN_no')
        widgets = {
            'customer_doc': forms.DateInput(attrs={'type': 'date'},),
            'customer_agreement_from': forms.DateInput(attrs={'type': 'date'},),
            'customer_agreement_to': forms.DateInput(attrs={'type': 'date'},),
        }


class CallAllocateForm(forms.ModelForm):
    def __init__(self,city, *args, **kwargs):
         super(CallAllocateForm, self).__init__(*args, **kwargs)
         if city:
             #print(city)
             self.fields['customer_id'].queryset = Customer.objects.filter(customer_city=city)
             self.fields['engg_id'].queryset = engg.objects.filter(engg_city=city)
         else:

            self.fields['customer_id'].queryset = Customer.objects.all()
            self.fields['engg_id'].queryset = engg.objects.all()

    p = products.objects.all()
    e = engg.objects.all()
    product = forms.ModelChoiceField(queryset=p,initial=0)
    class Meta:
        model = callallocate
        exclude = [
        'title',
        'comp_email',
        'phone_number',
        'cust_city',
        'complaint_no',
        'comp_address',
        'engg_name',
        'engg_contact',
        'engg_lat',
        'engg_long',
        'engg_rating',
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
        'engg_bus_end',
        'engg_bike_no',
        'engg_solve',
        'engg_part_name',
        'engg_part_no',
        'engg_feedback',
        'comp_rating',
        'comp_feedback',
        'engg_part_pic',
        'engg_bus_ticket_pic',
        'battery_percentage',
        'engg_start_reading_pic',
        'engg_end_reading_pic',
         ]

        fields = '__all__'
        labels = {
        'title':'Company Name',
        'comp_address':'company address',
        'comp_email':'company email',
        'description':'problem description',
        'start':'call start date',
        'engg_contact':'engineer contact no',
        'call_status':'status',
        'call_type':'category',
        'cust_city':'company city',
        'call_tat':'TAT',
        'call_note':'note',
        'call_priority':'priority',
        'caller_name':'name of caller',
        'engg_name':'engineer name',
        'engg_id':'engineer id',
        'engg_status':'engineer status',
        'end':'call end',

        }
        widgets = {
            'call_alloc_time': forms.TimeInput(attrs={'type':'time'}),
            'start': forms.DateInput(attrs={'type':'date'}),
            'end': forms.DateInput(attrs={'type':'date'}),

        }







class StockEntry(forms.ModelForm):
    class Meta:
        model = stock
        fields = '__all__'
        widgets = {
            'product_recieved_date': forms.DateInput(attrs={'type': 'date'}),
        }

class Product(forms.ModelForm):

    class Meta:
        model = products
        fields = "__all__"
