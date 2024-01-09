from django.db import models
from django.utils import timezone

from hotels.models import Room

class RoomService(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    SERVICES_TYPES = (
        ('Food', 'Food'),
        ('Cleaning', 'Cleaning'),
        ('Technical', 'Technical'),
    )
    services_type = models.CharField(max_length=20, choices=SERVICES_TYPES)
    created_date = models.DateField(default=timezone.now)
    price = models.FloatField()
    note = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return f'{self.room.number}-{self.services_type}'

    