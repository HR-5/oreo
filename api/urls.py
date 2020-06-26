from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'api'

urlpatterns = [
    url(r'^getschedule/(?P<schedule_id>[0-9a-f-])/$', views.get_schedule, name='getschedule'),
]
