from django.db import models
from datetime import datetime


# Create your models here.
class Schedule(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20)
    stime = models.TimeField(null=False, blank=False, default=datetime.now())
    etime = models.TimeField(null=False, blank=False, default=datetime.now())
    description = models.TextField(null=False, blank=False, max_length=200)
    location = models.CharField(null=False, blank=False, max_length=50)

    def __str__(self):
        return self.name
