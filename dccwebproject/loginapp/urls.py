from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name = 'loginapp'
urlpatterns = [
 url(r'^$',views.loginpage),
 url(r'^loggin/$',views.loggin, name='loggin'),
 url(r'^dash/$',views.dash ,name='dash'),
 url(r'^logout/$',views.logout ,name='logout'),
 url(r'^dash2/$',views.dash2 ,name='dash2'),
 url(r'^dash1/$',views.dash1 ,name='dash1'),
 url(r'^calendar/$',views.calendar,name='calendar'),
]
