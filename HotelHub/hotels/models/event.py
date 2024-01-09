from django.db import models

class Event(models.Model):
    eventType = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField()
    note = models.TextField(blank=True)
    price = models.FloatField()
    
    def __str__(self):
        return str(self.eventType)