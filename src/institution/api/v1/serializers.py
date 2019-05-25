from rest_framework import serializers

from institution.models import WorkingPlace


class WorkingPlaceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingPlace
        fields = ('id','name', 'street', 'country', 'city')
