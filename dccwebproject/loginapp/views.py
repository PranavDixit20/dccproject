from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect,HttpResponse
from . forms import RegisterForm
from . models import coadmin


def loginpage(request):
    return render(request,'loginapp/login.html')

@login_required
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
            user = form.save()
            user.refresh_from_db()
            user.coadmin.id = form.cleaned_data.get('coadmin_id')
            user.coadmin.name = form.cleaned_data.get('coadmin_name')
            user.coadmin.address = form.cleaned_data.get('coadmin_address')
            user.coadmin.email = form.cleaned_data.get('coadmin_email')
            user.coadmin.number = form.cleaned_data.get('coadmin_number')
            user.coadmin.telephone = form.cleaned_data.get('coadmin_telephone')
            user.coadmin.city = form.cleaned_data.get('coadmin_city')
            user.coadmin.branch_code = form.cleaned_data.get('coadmin_branch_code')
            user.coadmin.gender = form.cleaned_data.get('coadmin_gender')
            user.coadmin.bdate = form.cleaned_data.get('coadmin_bdate')
            user.coadmin.age = form.cleaned_data.get('coadmin_age')
            user.coadmin.joining_date = form.cleaned_data.get('coadmin_joining_date')
            user.coadmin.qualification = form.cleaned_data.get('coadmin_qualification')
            user.coadmin.designation = form.cleaned_data.get('coadmin_designation')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.name, password=raw_password)
            login(request,user)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request,'loginapp/register.html',{'form':form})
