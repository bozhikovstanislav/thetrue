#from kindofknowledge.api.v1.serializers import FieldOfScienceListSerializer
from professions.models import Profession
from rest_framework import serializers


class ProfessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profession
        fields = '__all__'
