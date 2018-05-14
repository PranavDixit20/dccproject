from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect,HttpResponse
from . forms import RegisterForm,EnggRegisterForm,CustomerRegisterForm,CallAllocateForm
from . models import engg,enggperformance
from . models import callallocate
from . models import coadmin
from . models import customer
import json
from . serializers import CallAllocateSerializer,EnggSerializer,EventCallSerializer
from django.core import serializers
from django.forms.models import model_to_dict


def index(request):
    return render(request,'loginapp/login.html')


def dash(request):
    return render(request,'loginapp/loggin/index.html')


def logout(request):
    return render(request,'loginapp/login.html')

def dash2(request):
    return render(request,'loginapp/index2.html')

def dash1(request):
    return render(request,'loginapp/index.html')

def calendar(request):
    return render(request,'loginapp/calendar.html')

def coregister(request):
    return render(request,'loginapp/coadmin_form.html')

def enggmap(request):
    data = enggperformance.objects.all()
    return render(request,'loginapp/enggmap.html',{'data':data})


def loggin(request):
        if request.method == 'POST':
            user = request.POST.get('username')
            pas = request.POST.get('password')
            form = AuthenticationForm(data=request.POST)

        if coadmin.objects.filter(co_name=user).exists() and coadmin.objects.filter(co_conf_pass=pas).exists():
            return render(request,'loginapp/index2.html')
        elif form.is_valid():
                return render(request,'loginapp/index.html')

        else:
                form = AuthenticationForm()
                return render(request,'loginapp/login.html',{'form':form})

def regcoadmin(request):

    if request.method == 'POST':
        coadminform = RegisterForm(request.POST,prefix='coadminform')

        if coadminform .is_valid():
            cname = coadminform.cleaned_data['name']
            cemail = coadminform.cleaned_data['email']
            cmobile = coadminform.cleaned_data['mobile_number']
            ctelephone = coadminform.cleaned_data['telephone_number']
            ccity = coadminform.cleaned_data['city']
            cbranch_code = coadminform.cleaned_data['branch_code']
            cgender = coadminform.cleaned_data['gender']
            cbirthdate = coadminform.cleaned_data['birth_date']
            cage = coadminform.cleaned_data['age']
            cjoining_date = coadminform.cleaned_data['joining_date']
            cqualification = coadminform.cleaned_data['qualification']
            cdesignation = coadminform.cleaned_data['designation']
            cpassword = coadminform.cleaned_data['password']
            ccpassword = coadminform.cleaned_data['confirm_password']
            caddress = coadminform.cleaned_data['address']

            coadmin.objects.create(
            co_name = cname,
            co_email = cemail,
            contact_number = cmobile,
            tell_no = ctelephone,
            co_city = ccity,
            branch_code = cbranch_code,
            co_gender = cgender,
            co_bdate = cbirthdate,
            co_age = cage,
            co_joining_date = cjoining_date,
            co_qual = cqualification,
            co_designation = cdesignation,
            co_pass = cpassword,
            co_conf_pass = ccpassword,
            co_address = caddress,
            ).save()


            return render(request,'loginapp/coadmin_form.html',{'coadminform':coadminform ,})
    else:
        coadminform = RegisterForm(prefix='coadminform')
    return render(request,'loginapp/coadmin_form.html',{'coadminform':coadminform })


def regengg(request):

        if request.method == 'POST':
            enggform = EnggRegisterForm(request.POST,request.FILES,prefix='enggform')
            if enggform.is_valid():
                ename = enggform.cleaned_data['name']
                eimage = enggform.cleaned_data['engg_photo']
                eemail = enggform.cleaned_data['email']
                emobile = enggform.cleaned_data['mobile_number']
                etelephone = enggform.cleaned_data['telephone_number']
                ecity = enggform.cleaned_data['city']
                ebranch_code = enggform.cleaned_data['branch_code']
                egender = enggform.cleaned_data['gender']
                ebirthdate = enggform.cleaned_data['birth_date']
                eage = enggform.cleaned_data['age']
                ejoining_date = enggform.cleaned_data['joining_date']
                equalification = enggform.cleaned_data['qualification']
                edesignation = enggform.cleaned_data['designation']
                eskill = enggform.cleaned_data['skills']
                epassword = enggform.cleaned_data['password']
                ecpassword = enggform.cleaned_data['confirm_password']
                eaddress = enggform.cleaned_data['address']
                pereaddress = enggform.cleaned_data['permanent_address']
                eid = enggform.cleaned_data['engg_id']

                engg.objects.create(
                engg_id = eid,
                engg_pic = eimage,
                engg_name = ename,
                engg_email = eemail,
                engg_address = eaddress,
                engg_permanent_address = pereaddress,
                engg_contact_number = emobile,
                engg_tell_no = etelephone,
                engg_city = ecity,
                engg_branch_code = ebranch_code,
                engg_gender = egender,
                engg_bdate = ebirthdate,
                engg_age = eage,
                engg_joining_date = ejoining_date,
                engg_qual = equalification,
                engg_designation = edesignation,
                engg_skill = eskill,
                engg_pass = epassword,
                engg_conf_pass = ecpassword,
                ).save()


                return render(request,'loginapp/register2.html',{'enggform':enggform,})
        else:
            enggform = EnggRegisterForm(prefix='enggform')
        return render(request,'loginapp/register2.html',{'enggform':enggform,})



def regcustom(request):

    if request.method == 'POST':
        customform = CustomerRegisterForm(request.POST,prefix='customform')

        if customform.is_valid():
            cuname = customform.cleaned_data['name']
            cuarea = customform.cleaned_data['area']
            culandmark = customform.cleaned_data['landmark']
            cucity = customform.cleaned_data['city']
            cupincode = customform.cleaned_data['pincode']
            cufaxno = customform.cleaned_data['fax_no']
            cucomptype = customform.cleaned_data['company_Type']
            cudoc = customform.cleaned_data['date_of_creation']
            cuemail = customform.cleaned_data['email']
            cucontact = customform.cleaned_data['contact_number']
            cuagreement = customform.cleaned_data['customer_agreement']
            cuamnt = customform.cleaned_data['agreement_amount']
            cupr1 = customform.cleaned_data['product1']
            cupr2 = customform.cleaned_data['product2']
            cupr3 = customform.cleaned_data['product3']
            cupr4 = customform.cleaned_data['product4']

            customer.objects.create(
            customer_name = cuname,
            customer_area = cuarea,
            customer_landmark = culandmark,
            customer_city = cucity,
            customer_pincode = cupincode,
            cutomer_fax = cufaxno,
            customer_compay_type = cucomptype,
            customer_doc = cudoc,
            customer_email = cuemail,
            customer_contact_no = cucontact,
            customer_agreement = cuagreement,
            customer_agreement_amount = cuamnt,
            customer_product1 = cupr1,
            customer_product2 = cupr2,
            customer_product3 = cupr3,
            customer_product4 = cupr4,
            ).save()

            return render(request,'loginapp/customregister.html',{'customform':customform,})

    else:
        customform = CustomerRegisterForm(prefix='customform')
        return render(request,'loginapp/customregister.html',{'customform':customform,})


def callallocation(request):

    if request.method == 'POST':
        callallocateform = CallAllocateForm(request.POST,prefix='callallocateform')

        if callallocateform.is_valid():
            compname = callallocateform.cleaned_data['company_name']
            compaddr = callallocateform.cleaned_data['company_address']
            compemail = callallocateform.cleaned_data['company_email']
            compcontact = callallocateform.cleaned_data['contact_number']
            compprob = callallocateform.cleaned_data['company_problem']
            calldate = callallocateform.cleaned_data['call_allocation_date']
            calltime = callallocateform.cleaned_data['call_allocation_time']
            enggname = callallocateform.cleaned_data['engg_name']
            enggid = callallocateform.cleaned_data['engg_id']
            enggcontact = callallocateform.cleaned_data['engg_contact']
            callstatus = callallocateform.cleaned_data['call_status']
            calltype = callallocateform.cleaned_data['call_type']
            compcty = callallocateform.cleaned_data['company_city']
            callautoclose = callallocateform.cleaned_data['call_auto_close_date']
            tat = callallocateform.cleaned_data['call_TAT']
            note = callallocateform.cleaned_data['call_note']
            cno = callallocateform.cleaned_data['complaint_no']
            prdct = callallocateform.cleaned_data['product']
            priority = callallocateform.cleaned_data['call_priority']
            caller = callallocateform.cleaned_data['caller_name']

            callallocate.objects.create(
            title = compname,
            comp_address = compaddr,
            comp_email = compemail,
            phone_number = compcontact,
            description = compprob,
            start = calldate,
            call_alloc_time = calltime,
            engg_name = enggname,
            engg_id = enggid,
            engg_contact = enggcontact,
            call_status = callstatus,
            call_type = calltype,
            cust_city = compcty,
            end = callautoclose,
            call_tat = tat,
            call_note = note,
            complaint_no = cno,
            product = prdct,
            call_prioriy = priority,
            caller_name = caller,
            ).save()

            return render(request,'loginapp/calendar.html')

    else:
        callallocateform = CallAllocateForm(prefix='callallocateform')
    return render(request,'loginapp/callallocate_form.html',{'callallocateform':callallocateform,})

class EventCallUpdateView(UpdateView):
    model = callallocate
    template_name = 'loginapp/callallocate_update.html'
    success_url = reverse_lazy('loginapp:calendar')
    fields = '__all__'

class EventCallDeleteView(DeleteView):
    model = callallocate
    success_url = reverse_lazy('loginapp:calendar')

class CallListView(generic.ListView):
    template_name = 'loginapp/calllist.html'
    context_object_name = 'callobj'

    def get_queryset(self):
        return callallocate.objects.all()

class CustomerListView(generic.ListView):
    template_name = 'loginapp/customerlist.html'
    context_object_name = 'customobj'

    def get_queryset(self):
        return customer.objects.all()

class CustomerDetailView(generic.DetailView):
    model = customer
    template_name = 'loginapp/customerdetail.html'

class CustomerUpdateView(UpdateView):
    model = customer
    template_name = 'loginapp/customer_update.html'
    success_url = reverse_lazy('loginapp:getcustomer')
    fields = ['customer_name','customer_area','customer_landmark','customer_city','customer_pincode',
            'cutomer_fax','customer_compay_type','customer_doc','customer_email','customer_contact_no',
             'customer_agreement','customer_agreement_amount','customer_product1','customer_product2',
             'customer_product3','customer_product4']

class CustomerDeleteView(DeleteView):
    model = customer
    success_url = reverse_lazy('loginapp:getcustomer')

class EnggListView(generic.ListView):
    template_name = 'loginapp/engglist.html'
    context_object_name = 'enggobj'

    def get_queryset(self):
        return engg.objects.all()

class DetailView(generic.DetailView):
    model = engg
    template_name = 'loginapp/enggdetail.html'

class CoadminListView(generic.ListView):
    template_name = 'loginapp/coadmin_list.html'
    context_object_name = 'coadminobj'

    def get_queryset(self):
        return coadmin.objects.all()

class EnggUpdateView(UpdateView):
    model = engg
    template_name = 'loginapp/engg_update.html'
    success_url = reverse_lazy('loginapp:getengg')
    fields = ['engg_pic','engg_name','engg_address','engg_email','engg_contact_number','engg_tell_no','engg_city','engg_branch_code','engg_gender','engg_bdate','engg_age','engg_joining_date',
    'engg_qual','engg_designation','engg_skill']
    success_message = 'data updated successfully!!!!'

class EnggDeleteView(DeleteView):
    model = engg
    success_url = reverse_lazy('loginapp:getengg')

class CoadminDetailView(generic.DetailView):
    model = coadmin
    template_name = 'loginapp/coadmindetail.html'


class CoadminUpdateView(UpdateView):
    model = coadmin
    template_name = 'loginapp/coadmin_update.html'
    success_url = reverse_lazy('loginapp:getcoadmin')
    fields = ['co_name','co_address','co_email','contact_number','tell_no','co_city','branch_code','co_gender','co_bdate','co_age','co_joining_date',
    'co_qual','co_designation']

class CoadminDeleteView(DeleteView):
    model = coadmin
    success_url = reverse_lazy('loginapp:getcoadmin')

class calllist(APIView):
    def get(self,request):
        callalloc = callallocate.objects.all()
        serializer = CallAllocateSerializer(callalloc,many=True)
        return Response(serializer.data)

class engglist(APIView):
    def get(self,request):
        callalloc = engg.objects.all()
        serializer = EnggSerializer(callalloc,many=True)
        return Response(serializer.data)

class eventcall(APIView):
    def get(self,request):
        callalloc = callallocate.objects.all()
        serializer = EventCallSerializer(callalloc,many=True)
        return Response(serializer.data)
