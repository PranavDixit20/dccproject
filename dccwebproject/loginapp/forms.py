from django import forms
from django.forms import ModelChoiceField
from . models import engg, stock, callallocate, customer, products, coadmin
from django.contrib.admin import widgets
import datetime







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
        exclude = []
        fields = '__all__'
        widgets = {
            'engg_bdate':forms.DateInput(attrs={'type':'date'}),
            'engg_joining_date':forms.DateInput(attrs={'type':'date'}),

        }

class CustomerRegisterForm(forms.ModelForm):
    q = products.objects.all()
    customer_product = forms.ModelChoiceField(queryset=q)
    class Meta:
        model = customer
        exclude = []
        fields = '__all__'
        widgets = {
            'customer_doc': forms.DateInput(attrs={'type': 'date'},),
        }


class CallAllocateForm(forms.ModelForm):
    qset = customer.objects.all()
    p = products.objects.all()
    e = engg.objects.all()
    cudate = datetime.datetime.now().strftime('%Y%m%d')
    c=cudate+""+str(callallocate.id)
    print(c)
    title = forms.ModelChoiceField(queryset=qset,initial=0)
    product = forms.ModelChoiceField(queryset=p,initial=0)
    engg_name = forms.ModelChoiceField(queryset=e,initial=0)
    complaint_no = forms.CharField(widget=forms.HiddenInput(), initial=c)

    class Meta:
        model = callallocate
        exclude = [
        'complaint_no',
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
        ]
        fields = '__all__'

        widgets = {
            'call_alloc_time': forms.TimeInput(attrs={'type':'time'}),
            'start': forms.TimeInput(attrs={'type':'date'}),
            'end': forms.TimeInput(attrs={'type':'date'}),

        }
        def __init__(self, *args, **kwargs):
             super(ProductForm, self).__init__(*args, **kwargs)
             self.fields['comp_address'] = company.objects.filter(customer_name=title).values_list('customer_address')



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
