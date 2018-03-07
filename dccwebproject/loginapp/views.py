from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect,HttpResponse


def loginpage(request):
    return render(request,'loginapp/login.html')

def dash(request):
    return render(request,'loginapp/loggin/index.html')

def loggin(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                return render(request,'loginapp/index.html')
            else:
                form = AuthenticationForm()
                return render(request,'loginapp/login.html',{'form':form})
