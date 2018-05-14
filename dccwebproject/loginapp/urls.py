from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login

app_name = 'loginapp'
urlpatterns = [
 url(r'^$',views.loginpage,name=index),
 url(r'^loggin/$',views.loggin, name='loggin'),
 url(r'^dash/$',views.dash ,name='dash'),
 url(r'^logout/$',views.logout ,name='logout'),
 url(r'^dash2/$',views.dash2 ,name='dash2'),
 url(r'^dash1/$',views.dash1 ,name='dash1'),
 url(r'^calendar/$',views.calendar,name='calendar'),
 url(r'^coregister/$',views.regcoadmin,name='regcoadmin'),
 url(r'^enggregister/$',views.regengg,name='regengg'),
 url(r'^customregister/$',views.regcustom,name='regcustom'),
 url(r'^engglist/$',views.EnggListView.as_view(),name='getengg'),
 url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='enggdetail'),
 url(r'^coadminlist/$',views.CoadminListView.as_view(),name='getcoadmin'),
 url(r'^customerlist/$',views.CustomerListView.as_view(),name='getcustomer'),
 url(r'customer/(?P<pk>[0-9]+)/detail/$',views.CustomerDetailView.as_view(),name='customerdetail'),
 url(r'customer/(?P<pk>[0-9]+)/$',views.CustomerUpdateView.as_view(),name='customerupdate'),
 url(r'customer/delete/(?P<pk>[0-9]+)/$',views.CustomerDeleteView.as_view(),name='customerdelete'),
 url(r'calendar/callallocate/$',views.callallocation,name='callallocation'),
 url(r'eventupdate/(?P<pk>[0-9]+)/$',views.EventCallUpdateView.as_view(),name='eventupdate'),
 url(r'eventdelete/delete/(?P<pk>[0-9]+)/$',views.EventCallDeleteView.as_view(),name='eventdelete'),
 url(r'^calllist/$',views.CallListView.as_view(),name='getcalllist'),
 url(r'coadmin/(?P<pk>[0-9]+)/detail/$',views.CoadminDetailView.as_view(),name='coadmindetail'),
 url(r'coadmin/(?P<pk>[0-9]+)/$',views.CoadminUpdateView.as_view(),name='coadminupdate'),
 url(r'coadmin/delete/(?P<pk>[0-9]+)/$',views.CoadminDeleteView.as_view(),name='coadmindelete'),
 url(r'engineer/(?P<pk>[0-9]+)/$',views.EnggUpdateView.as_view(),name='enggupdate'),
 url(r'engineer/delete/(?P<pk>[0-9]+)/$',views.EnggDeleteView.as_view(),name='enggdelete'),
 url(r'^enggmap/$',views.enggmap,name='enggmap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
