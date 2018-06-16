from django.conf import settings
from django.db.models import Q
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
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from . forms import RegisterForm,EnggRegisterForm,CustomerRegisterForm,CallAllocateForm,StockEntry,Product
from . models import engg,enggperformance
from . models import callallocate,products
from . models import coadmin
from . models import customer,stock
import json
import datetime
from . serializers import CallAllocateSerializer,EnggSerializer,EventCallSerializer,ChartSerializer
from django.core import serializers
from django.forms.models import model_to_dict
from tablib import Dataset
from .resources import EnggResource,CustomerResource,CoadminResource,CallallocateResource,StockResource

def update(request):
    return render(request,'loginapp/updateinfo.php')
def index(request):
    return render(request,'loginapp/login.html')

def callallocateexport_xls(request):
    person_resource = CallallocateResource()
    query = callallocate.objects.all()
    dataset = person_resource.export(query)
    response = HttpResponse(dataset.xls, content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="callallocate.xls"'
    return response
    render(request,'loginapp/calllist1.html')

def callallocateimport_xls(request):
        if request.method == 'POST':
            callallocate_resource = CallallocateResource()
            dataset = Dataset()
            new_persons = request.FILES['myfile']

            imported_data = dataset.load(new_persons.read())
            result = callallocate_resource.import_data(dataset, dry_run=True)  # Test the data import

            if not result.has_errors():
                callallocate_resource.import_data(dataset, dry_run=False)  # Actually import now

        return render(request, 'loginapp/stocklist.html')

def stockexport_xls(request):
    person_resource = StockResource()
    query = stock.objects.all()
    dataset = person_resource.export(query)
    response = HttpResponse(dataset.xls, content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="stock.xls"'
    return response
    render(request,'loginapp/stocklist.html')

def stockimport_xls(request):
        if request.method == 'POST':
            stock_resource = StockResource()
            dataset = Dataset()
            new_persons = request.FILES['myfile']

            imported_data = dataset.load(new_persons.read())
            result = stock_resource.import_data(dataset, dry_run=True)  # Test the data import

            if not result.has_errors():
                stock_resource.import_data(dataset, dry_run=False)  # Actually import now

        return render(request, 'loginapp/stocklist.html')

def coadminexport_xls(request):
    person_resource = CoadminResource()
    query = coadmin.objects.all()
    dataset = person_resource.export(query)
    response = HttpResponse(dataset.xls, content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="coadmin.xls"'
    return response
    render(request,'loginapp/coadmin_list.html')

def coadminimport_xls(request):
        if request.method == 'POST':
            coadmin_resource = CoadminResource()
            dataset = Dataset()
            new_persons = request.FILES['myfile']

            imported_data = dataset.load(new_persons.read())
            result = coadmin_resource.import_data(dataset, dry_run=True)  # Test the data import

            if not result.has_errors():
                coadmin_resource.import_data(dataset, dry_run=False)  # Actually import now

        return render(request, 'loginapp/coadmin_list.html')

def customerexport_xls(request):
    person_resource = CustomerResource()
    query = customer.objects.all()
    dataset = person_resource.export(query)
    response = HttpResponse(dataset.xls, content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="customer.xls"'
    return response
    render(request,'loginapp/customerlist1.html')

def customerimport_xls(request):
        if request.method == 'POST':
            customer_resource = CustomerResource()
            dataset = Dataset()
            new_persons = request.FILES['myfile']

            imported_data = dataset.load(new_persons.read())
            result = customer_resource.import_data(dataset, dry_run=True)  # Test the data import

            if not result.has_errors():
                customer_resource.import_data(dataset, dry_run=False)  # Actually import now
                return render(request, 'loginapp/customerlist1.html')
        return render(request, 'loginapp/customerlist1.html')


def enggexport_xls(request):

    person_resource = EnggResource()
    query = engg.objects.all()
    dataset = person_resource.export(query)
    response = HttpResponse(dataset.xls, content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response
    render(request,'loginapp/engglist1.html')



def enggimport_xls(request):
    if request.method == 'POST':
        engg_resource = EnggResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = engg_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            engg_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'loginapp/engglist1.html')

@login_required
def dash(request):
    return render(request,'loginapp/index.html')

def androidlogin(request):
    return render(request,'loginapp/index3.html')


def log_out(request):
    session = request.session.get('city')
    if session:
        del request.session['city']
        logout(request)
    else:
        logout(request)
    return render(request,'loginapp/login.html')

def dash2(request):

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
    city = request.session.get('city')
    data = callallocate.objects.filter(cust_city = city)
    return render(request,'loginapp/enggmap.html',{'data':data})

def enggmaps(request):
    data = callallocate.objects.all()
    return render(request,'loginapp/enggmap1.html',{'data':data})

def enggtrack(request,pk):
    data = callallocate.objects.filter(id=pk)
    return render(request,'loginapp/enggtrack.html',{'data':data})



def loggin(request):
        if request.method == 'POST':
            user = request.POST.get('username')
            pas = request.POST.get('password')
            city = request.POST.get('city')
            form = AuthenticationForm(data=request.POST)


            #return render(request,'loginapp/index2.html')
        if form.is_valid():
            usernm = authenticate(username=user,password=pas)
            if coadmin.objects.filter(co_name=user).exists() and coadmin.objects.filter(co_conf_pass=pas).exists() and coadmin.objects.filter(co_city=city).exists():

                request.session['city'] = city

                return render(request, 'loginapp/index2.html',)

            elif usernm.is_superuser:
                return render(request, 'loginapp/index.html')

            else:
                #messages.error(request, "all fields are mandatory")
                return render(request, 'loginapp/login.html', {'form': form})



        else:
                form = AuthenticationForm()
                return render(request, 'loginapp/login.html', {'form': form})

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

def productsave(request):
        if request.method == 'POST':
            form = Product(request.POST)
            if form.is_valid():
                form.save()
                prodobj = products.objects.all()
                return render(request,'loginapp/product_form.html',{'form':form,'prodobj':prodobj})
        else:
            form = Product()
            prodobj = products.objects.all()
            return render(request,'loginapp/product_form.html',{'form':form,'prodobj':prodobj})


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
        #form.fields['product_quantity'].queryset = stock.objects.aggregate(Sum('product_quantity'))
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
    form_class = StockEntry
    template_name = 'loginapp/stockupdate.html'
    success_url = reverse_lazy('loginapp:stocklist')


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
    model = callallocate
    def get_queryset(self):
        name = self.request.GET.get('q')
        if name:
            object_list = self.model.objects.filter(Q(call_status__icontains=name))
        else:
          city=self.request.session.get('city')
          object_list =  self.model.objects.filter(cust_city=city)
        return object_list

class Call1ListView(generic.ListView):
    template_name = 'loginapp/calllist1.html'
    context_object_name = 'callobjs'
    model = callallocate
    def get_queryset(self):
        name = self.request.GET.get('q')
        if name:
            object_list = self.model.objects.filter(Q(call_status__icontains=name))
        else:
            object_list = self.model.objects.all()
        return object_list

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
    model = customer
    def get_queryset(self):
        name = self.request.GET.get('q')
        if name:
            object_list = self.model.objects.filter(Q(customer_name__icontains=name))
        else:
            object_list = self.model.objects.all()
        return object_list

class CustomerDetailView(generic.DetailView):
    model = customer
    template_name = 'loginapp/customerdetail.html'

class Customer1DetailView(generic.DetailView):
    model = customer
    template_name = 'loginapp/customerdetail1.html'


class Customer1UpdateView(UpdateView):
    model = customer
    template_name = 'loginapp/customer_update1.html'
    success_url = reverse_lazy('loginapp:getcustomers')
    form_class = CustomerRegisterForm

class CustomerDeleteView(DeleteView):
    model = customer
    success_url = reverse_lazy('loginapp:getcustomer')

class Customer1DeleteView(DeleteView):
    model = customer
    success_url = reverse_lazy('loginapp:getcustomers')

class EnggListView(generic.ListView):
    template_name = 'loginapp/engglist.html'
    context_object_name = 'enggobj'
    model = engg

    def get_queryset(self):
         name = self.request.GET.get('q')
         if name:
            object_list = self.model.objects.filter(Q(engg_name__contains=name)
             | Q(engg_city__contains=name))
         else:
            city = self.request.session.get('city')
            object_list = engg.objects.filter(engg_city=city)
         return object_list


class Engg1ListView(generic.ListView):
    template_name = 'loginapp/engglist1.html'
    context_object_name = 'enggobjs'
    model = engg

    def get_queryset(self):

         name = self.request.GET.get('q')

         if name:
            object_list = self.model.objects.filter(engg_name__icontains = name)
         else:
            object_list = self.model.objects.all()
         return object_list


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
    form_class = EnggRegisterForm
    success_message = 'data updated successfully!!!!'

class Engg1UpdateView(UpdateView):
    model = engg
    template_name = 'loginapp/engg_update1.html'
    success_url = reverse_lazy('loginapp:getenggs')
    form_class = EnggRegisterForm
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
    form_class = RegisterForm
    template_name = 'loginapp/coadmin_update.html'
    success_url = reverse_lazy('loginapp:getcoadmin')


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


class ChartData(APIView):

    authentication_classes = ()
    permission_classes = ()
    def get(self, request):

        chartdata = customer.objects.all().count()

        return Response(chartdata)

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
