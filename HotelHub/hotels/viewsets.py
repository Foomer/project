from rest_framework import viewsets

from hotels.serializers import RoomSerializer,GuestSerializer,ReservationSerializer,ReservationViewSerializer,\
    EventSerializer,EventAttendeesViewSerializer,EventAttendeesSerializer
from hotels.models import Room,Guest,Reservation,Event,EventAttendees


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class GuestViewSet(viewsets.ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class = GuestSerializer
    
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReservationViewSerializer
        else:
            return ReservationSerializer
        
        
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class EventAttendeesViewSet(viewsets.ModelViewSet):
    queryset = EventAttendees.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EventAttendeesViewSerializer
        else:
            return EventAttendeesSerializer