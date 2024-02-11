from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    number = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=25,default='Standart')
    capacity = models.SmallIntegerField()
    floor = models.IntegerField()
    description = models.TextField()
    price_per_night = models.FloatField()
    check_in = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.number}-{self.type}'

