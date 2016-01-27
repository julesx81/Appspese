from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.viewPersonal, name='viewPersonal'),
    url(r'^provaApp/', views.viewExtended, name='viewExtended')
]
