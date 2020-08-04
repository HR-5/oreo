from django.db import models
from datetime import datetime


class Place(models.Model):
    name = models.CharField(null=True, blank=False, max_length=50)
    url = models.CharField(null=True, blank=False, max_length=50)
    description = models.TextField(null=False, blank=False, max_length=10000, default="Description")
    choices = {
        ('D', 'Department'),
        ('F', 'Food'),
        ('S', 'Sports'),
        ('A', 'Auditorium')
    }
    category = models.CharField(null=True, blank=False, choices=choices, max_length=50)
    imgname = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.name + " | " + self.get_category_display()


class Event(models.Model):
    name = models.CharField(null=True, blank=False, max_length=50)
    stime = models.TimeField(null=True, blank=False, default=datetime.now())
    etime = models.TimeField(null=True, blank=False, default=datetime.now())
    description = models.TextField(null=True, blank=False, max_length=1000)
    location = models.ForeignKey(Place, related_name='loc', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " - " + self.name


class DaySchedule(models.Model):
    date = models.DateField(null=True, blank=False)
    events = models.CharField(null=True, blank=False, max_length=500)

    def __str__(self):
        return self.date.strftime("%d %m %Y")
