from rest_framework import serializers

from hotels.models import Room,Guest,Reservation,Event,EventAttendees,Folio,FolioPosting,Payment

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class RoomSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model=Room
        fields=["user",'number','type','capacity','floor','description','price_per_night','check_in']
        
class GuestSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Guest
        fields=['id',"user",'first_name','middle_name','last_name','email','phone']
        
class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Reservation
        fields=['id',"user",'check_in_date','check_out_date','room','guest']
        
class ReservationViewSerializer(ReservationSerializer):
    room = RoomSerializer()
    guest = GuestSerializer(many=True)
    
    
class EventSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Event
        fields = ['id',"user",'event_type','location','start_date','end_date','note','price']
   
        
class EventAttendeesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = EventAttendees
        fields = ['id',"user",'event','number_of_dependees','guest']
        
class EventAttendeesViewSerializer(EventAttendeesSerializer):
    event = EventSerializer()
    guest = GuestSerializer()
    
    
        
class FolioPostingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = FolioPosting
        fields = ['id',"user",'folio','amount','department','note']    
        
            
class FolioSerializer(serializers.ModelSerializer):
    guest = GuestSerializer()
    folio_postings = FolioPostingSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Folio
        fields = ['id',"user",'guest','folio_postings']        
        
class PaymentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Payment
        fields = ['id',"user",'folio','type','amount','note']
        
class PaymentViewSerializer(PaymentSerializer):
    folio = FolioSerializer()
    

class RegistrationSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, user):
        token, _ = Token.objects.get_or_create(user=user)
        return token.key

    class Meta:
        model = User
        fields = ("username", "password", "token")
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user