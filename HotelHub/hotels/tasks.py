import logging
from HotelHub.celery import app
from datetime import datetime

from celery import shared_task
from hotels.models import Reservation

logger = logging.getLogger(__name__)


@shared_task
def clear_old_reservations():
    logger.error('hello')
    old_reservations = Reservation.objects.filter(check_out_date__lt=datetime.now())
    old_reservations.delete()