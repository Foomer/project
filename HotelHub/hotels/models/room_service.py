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
    servicesType = models.CharField(max_length=20, choices=SERVICES_TYPES)
    createdDate = models.DateField(default=timezone.now)
    price = models.FloatField()
    note = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.room.number}-{self.servicesType}'

    