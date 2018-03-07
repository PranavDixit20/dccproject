from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name = 'loginapp'
urlpatterns = [
 url(r'^$',views.loginpage),
 url(r'^loggin/$',views.loggin, name='loggin'),
 url(r'^dash/$',views.dash ,name='dash'),
]
