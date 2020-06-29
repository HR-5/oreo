from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'api'

urlpatterns = [
    url(r'^getschedule/$', views.get_schedule, name='getschedule'),
]
