from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import JsonResponse


def get_schedule(request, schedule_id):
    sch = get_object_or_404(Schedule, id=schedule_id)
    schdict = {
        'id': sch.id,
        'name': sch.name,
        'time': sch.time,
        'desc': sch.description,
        'loc': sch.location
    }
    print(schdict)
    return JsonResponse(schdict)