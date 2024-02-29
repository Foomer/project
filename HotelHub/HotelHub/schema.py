
import traceback

import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation

from django.contrib.auth.models import User

from hotels.models import Reservation,Guest,Room


class ReservationType(DjangoObjectType):
    class Meta:
        model = Reservation
        
class ReservationMutation(graphene.Mutation):
    class Arguments:
            user = graphene.ID(required=True)
            room = graphene.ID(required=True)
            guest = graphene.ID(required=True)
            check_in_date = graphene.Date(required=True)
            check_out_date = graphene.Date(required=True)

    reservation = graphene.Field(ReservationType)

    @classmethod
    def validate(cls, user,room, guest, check_in_date, check_out_date):
        if not room:
            raise Exception("Room ID is required")
        if not guest:
            raise Exception("Guest count is required")
        if not check_in_date:
            raise Exception('Check-in date is required')
        if not check_out_date:
            raise Exception('Check-out date is required')

    @classmethod
    def mutate(cls, root, info,user, room, guest, check_in_date, check_out_date):
        try:
            print("Running mutation")
            cls.validate(user,room, guest, check_in_date, check_out_date)
            room_instance = Room.objects.get(number=room)
            guest_instance = Guest.objects.get(id=guest)
            user_instance = User.objects.get(id=user)
    
            reservation = Reservation.objects.create(
                room = room_instance,
                user = user_instance,
                check_in_date = check_in_date,
                check_out_date = check_out_date,
                ) 
            reservation.guest.add(guest_instance)
        except Exception as e:
            traceback.print_exc()
            return ReservationMutation(reservation=None)

        return ReservationMutation(reservation=reservation)
    
    
class UpdateReservationMutation(graphene.Mutation):
    class Arguments:
        reservation_id = graphene.ID(required=True)
        check_in_date = graphene.Date()
        check_out_date = graphene.Date()

    reservation = graphene.Field(ReservationType)

    @staticmethod
    def mutate(root, info, reservation_id, check_in_date=None, check_out_date=None):
        try:
            
            reservation = Reservation.objects.get(id=reservation_id)
            
            if check_in_date:
                reservation.check_in_date = check_in_date
            if check_out_date:
                reservation.check_out_date = check_out_date

            
            reservation.save()

        except Reservation.DoesNotExist:
            
            return UpdateReservationMutation(reservation=None)

        
        return UpdateReservationMutation(reservation=reservation)
    
    
    
class ReservationNode(DjangoObjectType):
    class Meta:
        model = Reservation
        filter_fields = ['guest']
        interfaces = (relay.Node, )
    
class Mutation(graphene.ObjectType):
    create_reservation = ReservationMutation.Field()
    update_reservation = UpdateReservationMutation.Field()
    
class Query(graphene.ObjectType):
    reservation = relay.Node.Field(ReservationNode)
    
    all_reservayion = DjangoFilterConnectionField(ReservationNode)
    

schema = graphene.Schema(query=Query, mutation=Mutation)
        
        
        