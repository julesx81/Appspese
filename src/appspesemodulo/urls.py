from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^$', views.mesecorrente, name='mesecorrente'),
    url(r'^mesecorrente/', views.mesecorrente, name='mesecorrente'),
    url(r'^meseprecedente/', views.meseprecedente, name='meseprecedente')
]
