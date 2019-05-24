from rest_framework import serializers

from institution.models import WorkingPlace


class WorkingPlaceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingPlace
        fields = ('name', 'street', 'country', 'city')
