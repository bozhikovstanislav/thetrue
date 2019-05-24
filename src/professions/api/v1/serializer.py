from kindofknowledge.api.v1.serializer import FieldOfScienceListSerializer
from professions.models import Profession
from rest_framework import serializers


class ProfessionListSerializer(serializers.ListSerializer):
    field_of_science = FieldOfScienceListSerializer(many=True,blank=True)
    model = Profession
    fields = ('name', 'description', 'field_of_science')
