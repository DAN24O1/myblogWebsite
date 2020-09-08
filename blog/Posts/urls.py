from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^$', views.index, name ='index'),
    url(r'^(?P<topic>[0-9]+)/$',views.detail, name ="detail"),
    url(r'^(?P<topic>[0-9]+)/(?P<postId>[0-9]+)/?$',views.detail, name ="detail"),
    url('^cv/$', views.cv, name ='cv'),

]
