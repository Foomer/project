from django.db import models


from hotels.models import Room,Guest

class Reservation(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    guest = models.ManyToManyField(Guest)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    
    def __str__(self) -> str:
        guest_name = ', '.join([guest.first_name for guest in self.guest.all()])
        return f'Reservation for {guest_name} in {self.room.number} from {self.check_in_date} to {self.check_out_date}'


    