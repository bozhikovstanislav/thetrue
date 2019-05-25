from learningrooms.models import RoomQuizze
from rest_framework import serializers


class RoomQuizzesSerilizer(serializers.ModelSerializer):
    model = RoomQuizze
    fields = ('id','name','type_on_room','category','profession')
