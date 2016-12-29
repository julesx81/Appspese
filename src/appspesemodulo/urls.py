from django.conf.urls import url

from . import views

urlpatterns = [
#     url(r'^$', views.pagelogin, name='index'),
    url(r'^login/', views.pagelogin, name='login'),
    url(r'^logout/', views.my_logout, name='logout'),
    url(r'^mesecorrente/', views.currmonth, name='currmonth'),
    url(r'^meseprecedente/', views.lastmonth, name='lastmonth'),
    #url(r'^meseprecedente/', "appspesemodulo.views.lastmonth" ),
    url(r'^mesecustom/', views.custommonth, name='custommonth'),
    #url(r'^nomepagina/', "<appname>.views.<function_name>"),
]
