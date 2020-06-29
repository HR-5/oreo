from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import JsonResponse


def get_schedule(request):
    days = DaySchedule.objects.all()
    schedule = []
    for day in days:
        date = day.date
        event_ids = [int(i) for i in day.events.split("_")]
        events = []
        for evid in event_ids:
            event = Event.objects.get(id=evid)
            event_dict = {
                'name': event.name,
                'stime': event.stime.strftime("%H:%M"),
                'etime': event.etime.strftime("%H:%M"),
                'description': event.description,
                'location': event.location.name,
                'locurl': event.location.url
            }
            events.append(event_dict)
        day_dict = {
            'date': date.strftime("%m/%d/%Y"),
            'events' : events
        }
        schedule.append(day_dict)

    sch_dict = {
        'Time': datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        'schedule': schedule
    }
    return JsonResponse(sch_dict)
