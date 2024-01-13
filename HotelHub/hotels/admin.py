from django.contrib import admin

from hotels.models import Room,Guest,Reservation,Event,Folio,FolioPosting

# Register your models here.

admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Event)
admin.site.register(Folio)
admin.site.register(FolioPosting)