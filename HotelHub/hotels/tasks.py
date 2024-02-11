from HotelHub.celery import app
from datetime import datetime
from hotels.models import Reservation

@app.task(bind=True)
def clear_old_reservations(self):
    old_reservations = Reservation.objects.filter(check_out_date__lt=datetime.now())
    old_reservations.delete()
   