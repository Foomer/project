from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.TextField(blank=True)
    price = models.FloatField()
    
    def __str__(self):
        return str(self.event_type)