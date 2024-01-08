from rest_framework import serializers

from hotels.models import Room,Guest,Reservation

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=['number','type','capacity','floor','description','price_per_night']
        
class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields=['id','first_name','middle_name','last_name','email','phone']
        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields=['id','check_in_date','check_out_date','room','guest']
        
class ReservationViewSerializer(ReservationSerializer):
    room = RoomSerializer()
    guest = GuestSerializer(many=True)