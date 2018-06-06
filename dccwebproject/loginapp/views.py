from django.conf import settings
from django.db.models import Sum
import xlwt
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
from . models import customer,stock,Room
import json
import datetime
from . serializers import CallAllocateSerializer,EnggSerializer,EventCallSerializer
from django.core import serializers
from django.forms.models import model_to_dict
#coadcity = "abc"
city = "scv"

def index(request):
    return render(request,'loginapp/login.html')

def adminchat(request):
    rooms = Room.objects.order_by("title")

    # Render that in the index template
    return render(request, "loginapp/index.html", {
        "rooms": rooms,
    })
    #return render(request,'loginapp/index.html')

def export_xls(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=engineer.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("EnggSheet")

    row_num = 0

    columns = [
        "engg_id",
        "engg_name",
        "engg_address",
        "engg_email",
        "engg_contact_number",
        "engg_city",
        "engg_branch_code",
        "engg_gender",
        "engg_bdate",
        "engg_age",
        "engg_joining_date",
        "engg_qual",
        "engg_designation",
        "engg_skill",

    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width


    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1
    rows = engg.objects.all().values_list('engg_id','engg_name','engg_address','engg_email','engg_contact_number','engg_city','engg_branch_code','engg_gender','engg_bdate','engg_age','engg_joining_date','engg_qual','engg_designation','engg_skill')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

export_xls.short_description = u"Export XLS"

@login_required
def dash(request):
    return render(request,'loginapp/index.html')

def androidlogin(request):
    return render(request,'loginapp/index3.html')


def log_out(request):
    del request.session['city']
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
                ename = enggform.cleaned_data['engg_name']
                eemail = enggform.cleaned_data['engg_email']
                epassword = enggform.cleaned_data['engg_pass']
                conpassword = enggform.cleaned_data['engg_conf_pass']
                if epassword == conpassword:
                 enggform.save()
                 User.objects.create_user(ename, eemail, epassword)
                 user = authenticate(username=ename, password=epassword)
                 login(request, user)
                 subject = 'Registration successfull!!'
                 message = 'Your Registration is successfull!!\n your username is '+str(ename)+'password is '+'epassword'+''

                 from_email = settings.EMAIL_HOST_USER
                 to_list = [eemail,settings.EMAIL_HOST_USER]
                 send_mail(subject,message,from_email,to_list,fail_silently = True)

                 return render(request,'loginapp/register1.html',{'enggform':enggform,})
                else:
                    return HttpResponse("<div>passwords do not match!!!</div>")

        else:
            enggform = EnggRegisterForm(prefix='enggform')
        return render(request,'loginapp/register1.html',{'enggform':enggform,})


def regcustoms(request):

    if request.method == 'POST':
        customform = CustomerRegisterForm(request.POST,prefix='customform')

        if customform.is_valid():
            customform.save()

            return render(request,'loginapp/customregister1.html',{'customform':customform,})

    else:
        customform = CustomerRegisterForm(prefix='customform')
        return render(request,'loginapp/customregister1.html',{'customform':customform,})


def callallocation(request):

    if request.method == 'POST':
        callallocateform = CallAllocateForm(request.POST,prefix='callallocateform')
        cno = callallocateform.cleaned_data['complaint_no']
        if callallocateform.is_valid():
            callallocateform.save()

            subject = 'Call Allocated'
            message = 'Your call has been allocated successfully!!\n your complaint no. is '+cno+''

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
            cudate = datetime.datetime.now()
            #callid = callallocate.objects.get()
            callallocateform.cleaned_data['complaint_id'] = cudate
            callallocateform.save()


            print (cudate)
            #print(callid)
            compemail = callallocateform.cleaned_data['comp_email']
            subject = 'Call Allocated'
            message = 'Your call has been allocated successfully!!\n your complaint no. is '+str(cudate)+''

            from_email = settings.EMAIL_HOST_USER
            to_list = [compemail,settings.EMAIL_HOST_USER]
            send_mail(subject,message,from_email,to_list,fail_silently = True)

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
        city=self.request.session.get('city')
        if city:
          return callallocate.objects.filter(cust_city=city)
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
        city=self.request.session.get('city')
        if city:
         callalloc =  callallocate.objects.filter(cust_city=city)
         serializer = EventCallSerializer(callalloc,many=True)
        else:
            callalloc =  callallocate.objects.all()
            serializer = EventCallSerializer(callalloc,many=True)
        return Response(serializer.data)
