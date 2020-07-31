from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'api'

urlpatterns = [
    url(r'^getdetails/$', views.get_details, name='get_details'),
]
