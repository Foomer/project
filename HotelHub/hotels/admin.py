from django.contrib import admin

from hotels.models import Room,Guest,Reservation,RoomService,Event

# Register your models here.

admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(RoomService)
admin.site.register(Event)