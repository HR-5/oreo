from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import JsonResponse


def create_img_name():
    places = Place.objects.all()
    for place in places:
        name = place.name.lower().split(' ')
        imgname = '_'.join(name)
        place.imgname = imgname
        place.save()


def get_places():
    # create_img_name()
    places = Place.objects.all()
    food_stalls = []
    department = []
    sports = []
    for place in places:
        p_dict = {
            'name': place.name,
            'locurl': place.url,
            'imgurl': place.imgname,
            'description': place.description
        }
        if place.category == 'S':
            sports.append(p_dict)
        elif place.category == 'D':
            department.append(p_dict)
        elif place.category == 'F':
            food_stalls.append(p_dict)

    places = [food_stalls, department, sports]
    return places


def get_schedule():
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
                'locurl': event.location.url,
                'imgname': event.location.imgname
            }
            events.append(event_dict)
        day_dict = {
            'date': date.strftime("%d %B %Y"),
            'events': events
        }
        schedule.append(day_dict)

    return schedule


def get_details(request):
    places = get_places()
    schedule = get_schedule()
    details_dict = {
        'time': datetime.now().strftime("%m %B %Y, %H:%M:%S"),
        'schedule': schedule,
        'food': places[0],
        'department': places[1],
        'sports': places[2],
    }
    return JsonResponse(details_dict)
