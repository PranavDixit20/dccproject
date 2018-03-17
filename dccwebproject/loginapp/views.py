from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect,HttpResponse
from . forms import RegisterForm
from . models import coadmin


def loginpage(request):
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
    return render(request,'loginapp/register.html')

def loggin(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                return render(request,'loginapp/index.html')
            else:
                form = AuthenticationForm()
                return render(request,'loginapp/login.html',{'form':form})

def regcoadmin(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            id = form.cleaned_data['coadmin_id']
            name = form.cleaned_data['coadmin_name']
            address = form.cleaned_data['coadmin_address']
            email = form.cleaned_data['coadmin_email']
            number = form.cleaned_data['coadmin_number']
            telephone = form.cleaned_data['coadmin_telephone']
            city = form.cleaned_data['coadmin_city']
            branch_code = form.cleaned_data['coadmin_branch_code']
            gender = form.cleaned_data['coadmin_gender']
            bdate = form.cleaned_data['coadmin_bdate']
            age = form.cleaned_data['coadmin_age']
            joining_date = form.cleaned_data['coadmin_joining_date']
            qualification = form.cleaned_data['coadmin_qualification']
            designation = form.cleaned_data['coadmin_designation']
            photo = form.cleaned_data['coadmin_photo']
            password = form.cleaned_data['coadmin_password']
            conf_password = form.cleaned_data['coadmin_conf_pass']

            coadmin.objects.create(
            co_id=id,
            co_name=name,
            co_address=address,
            co_email=email,
            contact_number=number,
            tell_no=telephone,
            co_city=city,
            branch_code=branch_code,
            co_gender=gender,
            co_bdate=bdate,
            co_age=age,
            co_joining_date=joining_date,
            co_qual=qualification,
            co_designation=designation,
            co_photo=ImageModel(co_photo=request.FILES['co_photo']),
            co_pass=password,
            co_conf_pass=conf_password,
            ).save()
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request,'loginapp/register.html',{'form':form})
