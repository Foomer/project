from rest_framework import viewsets

from hotels.serializers import RoomSerializer,GuestSerializer,ReservationSerializer,ReservationViewSerializer
from hotels.models import Room,Guest,Reservation


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