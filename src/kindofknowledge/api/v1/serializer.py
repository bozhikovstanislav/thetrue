from kindofknowledge.models import FieldOfScience
from rest_framework import serializers


class FieldOfScienceListSerializer(serializers.ListSerializer):
    model = FieldOfScience
    fields = ('name', 'description')
