from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib.auth.views import login

app_name = 'loginapp'
urlpatterns = [
 url(r'^androidlogin/$',views.androidlogin,name='androidlogin'),
 url(r'^$',views.index,name='index'),
 url(r'^loggin/$',views.loggin, name='loggin'),
 url(r'^dash/$',views.dash ,name='dash'),
 url(r'^logout/$',views.log_out ,name='logout'),
 url(r'^dash2/$',views.dash2 ,name='dash2'),
 url(r'^dash1/$',views.dash1 ,name='dash1'),
 url(r'dash1/stockentry/$',views.stockentry ,name='stockentry'),
 url(r'^calendar/$',views.calendar,name='calendar'),
 url(r'^calendars/$',views.calendars,name='calendars'),
 url(r'^coregister/$',views.regcoadmin,name='regcoadmin'),
 url(r'^enggregister/$',views.regengg,name='regengg'),
 url(r'^enggregisters/$',views.regenggs,name='regenggs'),
 url(r'^customregister/$',views.regcustom,name='regcustom'),
 url(r'^customregisters/$',views.regcustoms,name='regcustoms'),
 url(r'engglist/$',views.EnggListView.as_view(),name='getengg'),
 url(r'dash1/stocklist/$',views.StockListView.as_view(),name='stocklist'),
 url(r'^engglist1/$',views.Engg1ListView.as_view(),name='getenggs'),
 url(r'enggdetail/(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='enggdetail'),
 url(r'dash1/stockdetail/(?P<pk>[0-9]+)/$',views.StockDetailView.as_view(),name='stockdetail'),
 url(r'dash1/stockupdate/(?P<pk>[0-9]+)/$',views.StockUpdateView.as_view(),name='stockupdate'),
 url(r'stockdelete/delete/(?P<pk>[0-9]+)/$',views.StockDeleteView.as_view(),name='stockdelete'),
 url(r'^(?P<pk>[0-9]+)/$',views.Detail1View.as_view(),name='enggdetails'),
 url(r'^coadminlist/$',views.CoadminListView.as_view(),name='getcoadmin'),
 url(r'^customerlist/$',views.CustomerListView.as_view(),name='getcustomer'),
 url(r'^customerlist1/$',views.Customer1ListView.as_view(),name='getcustomers'),
 url(r'customer/(?P<pk>[0-9]+)/detail/$',views.CustomerDetailView.as_view(),name='customerdetail'),
 url(r'customer1/(?P<pk>[0-9]+)/detail/$',views.Customer1DetailView.as_view(),name='customerdetails'),
 url(r'customer/(?P<pk>[0-9]+)/$',views.CustomerUpdateView.as_view(),name='customerupdate'),
 url(r'customer1/(?P<pk>[0-9]+)/$',views.Customer1UpdateView.as_view(),name='customerupdates'),
 url(r'customer/delete/(?P<pk>[0-9]+)/$',views.CustomerDeleteView.as_view(),name='customerdelete'),
 url(r'customer1/delete/(?P<pk>[0-9]+)/$',views.Customer1DeleteView.as_view(),name='customerdeletes'),
 url(r'calendar/callallocate/$',views.callallocation,name='callallocation'),
 url(r'calendar/callallocate1/$',views.callallocations,name='callallocations'),
 url(r'eventupdate/(?P<pk>[0-9]+)/$',views.EventCallUpdateView.as_view(),name='eventupdate'),
 url(r'eventupdate1/(?P<pk>[0-9]+)/$',views.EventCall1UpdateView.as_view(),name='eventupdates'),
 url(r'eventdelete/delete/(?P<pk>[0-9]+)/$',views.EventCallDeleteView.as_view(),name='eventdelete'),
 url(r'eventdelete1/delete/(?P<pk>[0-9]+)/$',views.EventCall1DeleteView.as_view(),name='eventdeletes'),
 url(r'^calllist/$',views.CallListView.as_view(),name='getcalllist'),
 url(r'^calllist1/$',views.Call1ListView.as_view(),name='getcalllists'),
 url(r'coadmin/(?P<pk>[0-9]+)/detail/$',views.CoadminDetailView.as_view(),name='coadmindetails'),
 url(r'coadmin/(?P<pk>[0-9]+)/$',views.CoadminUpdateView.as_view(),name='coadminupdate'),
 url(r'coadmin/delete/(?P<pk>[0-9]+)/$',views.CoadminDeleteView.as_view(),name='coadmindelete'),
 url(r'engineer/(?P<pk>[0-9]+)/$',views.EnggUpdateView.as_view(),name='enggupdate'),
 url(r'engineers/(?P<pk>[0-9]+)/$',views.Engg1UpdateView.as_view(),name='enggupdates'),
 url(r'engineer/delete/(?P<pk>[0-9]+)/$',views.EnggDeleteView.as_view(),name='enggdelete'),
 url(r'engineers/delete/(?P<pk>[0-9]+)/$',views.Engg1DeleteView.as_view(),name='enggdeletes'),
 url(r'^enggmap/$',views.enggmap,name='enggmap'),
 url(r'^enggmap1/$',views.enggmaps,name='enggmaps'),
 #url(r'search/$',views.search,name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
