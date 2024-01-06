from django.db import models


class Room(models.Model):
    number = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=25,default='Standart')
    capacity = models.SmallIntegerField()
    floor = models.IntegerField()
    description = models.TextField()
    price_per_night = models.FloatField()
    
    def __str__(self) -> str:
        return f'{self.number}-{self.type}'

