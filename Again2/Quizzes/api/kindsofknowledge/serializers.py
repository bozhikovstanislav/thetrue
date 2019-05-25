from kindsofknowledge.models import FieldOfScience

from rest_framework import serializers


class FieldOfScienceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = FieldOfScience
        fields = ('name','description')