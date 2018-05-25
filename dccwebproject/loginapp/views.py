from django.conf import settings
from django.db.models import Sum
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
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
from . forms import RegisterForm,EnggRegisterForm,CustomerRegisterForm,CallAllocateForm,StockEntry
from . models import engg,enggperformance
from . models import callallocate
from . models import coadmin
from . models import customer,stock
import json
from . serializers import CallAllocateSerializer,EnggSerializer,EventCallSerializer
from django.core import serializers
from django.forms.models import model_to_dict
#coadcity = "abc"
city = "scv"

def index(request):
    return render(request,'loginapp/login.html')

@login_required
def dash(request):
    return render(request,'loginapp/loggin/index.html')

def androidlogin(request):
    return render(request,'loginapp/index3.html')


def log_out(request):
    logout(request)
    return render(request,'loginapp/login.html')

def dash2(request):
    print(city)
    return render(request,'loginapp/index2.html')

def dash1(request):
    return render(request,'loginapp/index.html')

def calendar(request):
    return render(request,'loginapp/calendar.html')

def calendars(request):
    return render(request,'loginapp/calendar1.html')

def coregister(request):
    return render(request,'loginapp/coadmin_form.html')

def enggmap(request):
    data = enggperformance.objects.all()
    return render(request,'loginapp/enggmap.html',{'data':data})

def enggmaps(request):
    data = enggperformance.objects.all()
    return render(request,'loginapp/enggmap1.html',{'data':data})



def loggin(request):
        if request.method == 'POST':
            user = request.POST.get('username')
            pas = request.POST.get('password')
            city = request.POST.get('city')
            form = AuthenticationForm(data=request.POST)


            #return render(request,'loginapp/index2.html')
        if form.is_valid() :
            usernm = authenticate(username=user,password=pas)
            if coadmin.objects.filter(co_name=user).exists() and coadmin.objects.filter(co_conf_pass=pas).exists() and coadmin.objects.filter(co_city=city).exists():

                request.session['city']=city
                print(city)
                return render(request,'loginapp/index2.html',)

            elif usernm.is_superuser:
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
            User.objects.create_user(cname, cemail, cpassword)
            user = authenticate(username=cname, password=cpassword)
            login(request, user)
            subject = 'Co-Admin added'
            message = 'Co-Admin has been Registered successfully!!\n your name is '+str(cname)+' and password is '+str(cpassword)+''
            from_email = settings.EMAIL_HOST_USER
            to_list = [compemail,settings.EMAIL_HOST_USER]
            send_mail(subject,message,from_email,to_list,fail_silently = True)
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
                ecity = city
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

def regenggs(request):

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
                estatus = enggform.cleaned_data['status']

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
                engg_status = estatus,
                ).save()
                User.objects.create_user(ename, eemail, epassword)
                user = authenticate(username=ename, password=epassword)
                login(request, user)

                return render(request,'loginapp/register1.html',{'enggform':enggform,})
        else:
            enggform = EnggRegisterForm(prefix='enggform')
        return render(request,'loginapp/register1.html',{'enggform':enggform,})

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

def regcustoms(request):

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

            return render(request,'loginapp/customregister1.html',{'customform':customform,})

    else:
        customform = CustomerRegisterForm(prefix='customform')
        return render(request,'loginapp/customregister1.html',{'customform':customform,})


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
            enggstatus = callallocateform.cleaned_data['engg_status']
            enggcontact = callallocateform.cleaned_data['engg_contact']
            callstatus = callallocateform.cleaned_data['call_status']
            calltype = callallocateform.cleaned_data['call_type']
            compcty = callallocateform.cleaned_data['company_city']
            callautoclose = callallocateform.cleaned_data['call_auto_close_date']
            tat = callallocateform.cleaned_data['call_TAT']
            note = callallocateform.cleaned_data['call_note']
            prdct = callallocateform.cleaned_data['product']
            priority = callallocateform.cleaned_data['call_priority']
            caller = callallocateform.cleaned_data['caller_name']

            print(compname)
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
            engg_status = enggstatus,
            engg_contact = enggcontact,
            call_status = callstatus,
            call_type = calltype,
            cust_city = compcty,
            end = callautoclose,
            call_tat = tat,
            call_note = note,
            product = prdct,
            call_prioriy = priority,
            caller_name = caller,
            ).save()

            subject = 'Call Allocated'
            message = 'Your call has been allocated successfully!!\n your complaint no. is '+str(cno)+''

            from_email = settings.EMAIL_HOST_USER
            to_list = [compemail,settings.EMAIL_HOST_USER]
            send_mail(subject,message,from_email,to_list,fail_silently = True)
            return render(request,'loginapp/calendar.html')

    else:
        callallocateform = CallAllocateForm(prefix='callallocateform')
    return render(request,'loginapp/callallocate_form.html',{'callallocateform':callallocateform,})

def callallocations(request):

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
            enggstatus = callallocateform.cleaned_data['engg_status']
            enggcontact = callallocateform.cleaned_data['engg_contact']
            callstatus = callallocateform.cleaned_data['call_status']
            calltype = callallocateform.cleaned_data['call_type']
            compcty = callallocateform.cleaned_data['company_city']
            callautoclose = callallocateform.cleaned_data['call_auto_close_date']
            tat = callallocateform.cleaned_data['call_TAT']
            note = callallocateform.cleaned_data['call_note']
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
            engg_status = enggstatus,
            engg_contact = enggcontact,
            call_status = callstatus,
            call_type = calltype,
            cust_city = compcty,
            end = callautoclose,
            call_tat = tat,
            call_note = note,
            product = prdct,
            call_prioriy = priority,
            caller_name = caller,
            ).save()
            print(compname)

            return render(request,'loginapp/calendar1.html')
    else:
        callallocateform = CallAllocateForm(prefix='callallocateform')
    return render(request,'loginapp/callallocate_form1.html',{'callallocateform':callallocateform,})

def stockentry(request):
    if request.method == 'POST':
        form = StockEntry(request.POST)

        if form.is_valid():
            form.save()
            return render(request,'loginapp/stockentry.html',{'form':form})
    else:
        form = StockEntry()
        form.fields['product_quantity'].queryset = stock.objects.aggregate(Sum('product_quantity'))
        return render(request,'loginapp/stockentry.html',{'form':form})

class StockListView(generic.ListView):
    template_name = 'loginapp/stocklist.html'
    context_object_name = 'stockobj'

    def get_queryset(self):
        return stock.objects.all()

class StockDetailView(generic.DetailView):
    model = stock
    template_name = 'loginapp/stockdetail.html'

class StockUpdateView(UpdateView):
    model = stock
    template_name = 'loginapp/stockupdate.html'
    success_url = reverse_lazy('loginapp:stocklist')
    fields = '__all__'

class StockDeleteView(DeleteView):
    model = stock
    success_url = reverse_lazy('loginapp:stocklist')

class EventCallUpdateView(UpdateView):
    model = callallocate
    template_name = 'loginapp/callallocate_update.html'
    success_url = reverse_lazy('loginapp:calendar')
    fields = '__all__'

class EventCall1UpdateView(UpdateView):
    model = callallocate
    template_name = 'loginapp/callallocate_update1.html'
    success_url = reverse_lazy('loginapp:calendars')
    fields = '__all__'

class EventCallDeleteView(DeleteView):
    model = callallocate
    success_url = reverse_lazy('loginapp:calendar')

class EventCall1DeleteView(DeleteView):
    model = callallocate
    success_url = reverse_lazy('loginapp:calendars')

class CallListView(generic.ListView):
    template_name = 'loginapp/calllist.html'
    context_object_name = 'callobj'

    def get_queryset(self):
        return callallocate.objects.all()

class Call1ListView(generic.ListView):
    template_name = 'loginapp/calllist1.html'
    context_object_name = 'callobjs'

    def get_queryset(self):
        return callallocate.objects.all()

class CustomerListView(generic.ListView):
    template_name = 'loginapp/customerlist.html'
    context_object_name = 'customobj'

    def get_queryset(self):
        city=self.request.session.get('city')
        if city:
          return customer.objects.filter(customer_city=city)
        return customer.objects.all()

class Customer1ListView(generic.ListView):
    template_name = 'loginapp/customerlist1.html'
    context_object_name = 'customobjs'

    def get_queryset(self):
        return customer.objects.all()

class CustomerDetailView(generic.DetailView):
    model = customer
    template_name = 'loginapp/customerdetail.html'

class Customer1DetailView(generic.DetailView):
    model = customer
    template_name = 'loginapp/customerdetail1.html'

class CustomerUpdateView(UpdateView):
    model = customer
    template_name = 'loginapp/customer_update.html'
    success_url = reverse_lazy('loginapp:getcustomer')
    fields = '__all__'

class Customer1UpdateView(UpdateView):
    model = customer
    template_name = 'loginapp/customer_update1.html'
    success_url = reverse_lazy('loginapp:getcustomers')
    fields = '__all__'

class CustomerDeleteView(DeleteView):
    model = customer
    success_url = reverse_lazy('loginapp:getcustomer')

class Customer1DeleteView(DeleteView):
    model = customer
    success_url = reverse_lazy('loginapp:getcustomers')

class EnggListView(generic.ListView):
    template_name = 'loginapp/engglist.html'
    context_object_name = 'enggobj'


    def get_queryset(self):
        city=self.request.session.get('city')
        if city:
         return engg.objects.filter(engg_city=city)
        return engg.objects.all()

class Engg1ListView(generic.ListView):
    template_name = 'loginapp/engglist1.html'
    context_object_name = 'enggobjs'

    def get_queryset(self):
        return engg.objects.all()

class DetailView(generic.DetailView):
    model = engg
    template_name = 'loginapp/enggdetail.html'

class Detail1View(generic.DetailView):
    model = engg
    template_name = 'loginapp/enggdetail1.html'

class CoadminListView(generic.ListView):
    template_name = 'loginapp/coadmin_list.html'
    context_object_name = 'coadminobj'

    def get_queryset(self):
        return coadmin.objects.all()

class EnggUpdateView(UpdateView):
    model = engg
    template_name = 'loginapp/engg_update.html'
    success_url = reverse_lazy('loginapp:getengg')
    fields = '__all__'
    success_message = 'data updated successfully!!!!'

class Engg1UpdateView(UpdateView):
    model = engg
    template_name = 'loginapp/engg_update1.html'
    success_url = reverse_lazy('loginapp:getenggs')
    fields = '__all__'
    success_message = 'data updated successfully!!!!'

class EnggDeleteView(DeleteView):
    model = engg
    success_url = reverse_lazy('loginapp:getengg')

class Engg1DeleteView(DeleteView):
    model = engg
    success_url = reverse_lazy('loginapp:getenggs')

class CoadminDetailView(generic.DetailView):
    model = coadmin
    template_name = 'loginapp/coadmindetail.html'


class CoadminUpdateView(UpdateView):
    model = coadmin
    template_name = 'loginapp/coadmin_update.html'
    success_url = reverse_lazy('loginapp:getcoadmin')
    fields = '__all__'

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
