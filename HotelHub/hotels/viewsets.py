from rest_framework import viewsets

from hotels.serializers import RoomSerializer,GuestSerializer,ReservationSerializer,ReservationViewSerializer,\
    EventSerializer,EventAttendeesViewSerializer,EventAttendeesSerializer,FolioSerializer,FolioPostingSerializer,PaymentSerializer,PaymentViewSerializer
    
from hotels.models import Room,Guest,Reservation,Event,EventAttendees,Folio,FolioPosting,Payment

from django_filters.rest_framework import DjangoFilterBackend

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['number','type']
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    
class GuestViewSet(viewsets.ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class = GuestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name','last_name']
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReservationViewSerializer
        else:
            return ReservationSerializer
        
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['guest']
        
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
        
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
class EventAttendeesViewSet(viewsets.ModelViewSet):
    queryset = EventAttendees.objects.all()
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EventAttendeesViewSerializer
        else:
            return EventAttendeesSerializer
        

class FolioViewSet(viewsets.ModelViewSet):
    queryset = Folio.objects.all()
    serializer_class = FolioSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['guest']
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
class FolioPostingViewSet(viewsets.ModelViewSet):
    queryset = FolioPosting.objects.all()
    serializer_class = FolioPostingSerializer
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PaymentViewSerializer
        else:
            return PaymentSerializer