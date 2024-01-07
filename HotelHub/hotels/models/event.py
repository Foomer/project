from django.db import models

class Event(models.Model):
    EVENT_TYPES = (
        ('Movie', 'Movie'),
        ('Theater', 'Theater'),
        ('Conference', 'Conference'),
        ('Concert', 'Concert'),
        ('Entertainment', 'Entertainment'),
        ('Live Music', 'Live Music'),
    )
    eventType = models.CharField(max_length=20, choices=EVENT_TYPES)
    location = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField()
    note = models.TextField(blank=True)
    price = models.FloatField()
    
    def __str__(self):
        return str(self.eventType)