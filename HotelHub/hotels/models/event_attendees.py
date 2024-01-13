from django.db import models

from hotels.models import Event,Guest

class EventAttendees(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    number_of_dependees = models.IntegerField(default=0)
    guest = models.ForeignKey(Guest,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.event} {self.guest}'