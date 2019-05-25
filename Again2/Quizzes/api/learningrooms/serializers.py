from rest_framework import serializers

from learningrooms.models import RoomQuizze


class RoomQuizzesSerilizer(serializers.ModelSerializer):
    model = RoomQuizze
    fields = ('id', 'name', 'type_on_room', 'category', 'profession')
