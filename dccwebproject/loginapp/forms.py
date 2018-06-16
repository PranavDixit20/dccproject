from django import forms
from django.forms import ModelChoiceField
from . models import engg, stock, callallocate, customer, products, coadmin






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
    title = forms.ModelChoiceField(queryset=qset)
    product = forms.ModelChoiceField(queryset=p)
    engg_lat = forms.DecimalField(initial=0.0)
    engg_long = forms.DecimalField(initial=0.0)

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
        ]
        fields = '__all__'
        widgets = {
            'call_alloc_time': forms.TimeInput(attrs={'type':'time'}),
            'start': forms.DateInput(attrs={'type':'date'}),
            'end': forms.TimeInput(attrs={'type':'date'}),
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
