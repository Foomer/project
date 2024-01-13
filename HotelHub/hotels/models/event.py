from django.db import models

class Event(models.Model):
    event_type = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.TextField(blank=True)
    price = models.FloatField()
    
    def __str__(self):
        return str(self.event_type)