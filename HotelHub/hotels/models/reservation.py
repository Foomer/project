from django.db import models
from django.core.exceptions import ValidationError

from hotels.models import Guest

class Reservation(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    room = models.ForeignKey('hotels.Room',on_delete=models.CASCADE)
    guest = models.ManyToManyField(Guest)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    
    def save(self, *args, **kwargs):
        if Reservation.objects.filter(room=self.room).filter(check_in_date__lte=self.check_out_date).filter(check_out_date__gte=self.check_in_date).exists():
            raise ValidationError('This reservation conflicts with existing reservations for this room.')
        super().save(*args, **kwargs)
    def __str__(self) -> str:
        guest_name = ', '.join([guest.first_name for guest in self.guest.all()])
        return f'Reservation for {guest_name} in {self.room.number} from {self.check_in_date} to {self.check_out_date}'


    