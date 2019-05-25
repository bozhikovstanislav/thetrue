from kindofknowledge.models import FieldOfScience
#from professions.api.v1.serializers import ProfessionSerializer
from rest_framework import serializers


class FieldOfScienceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = FieldOfScience
        fields = ('name','description')
