from rest_framework import generics

from .serializers import WorkingPlaceDetailSerializer
from institution.models import WorkingPlace


class WorkingDetailView(generics.ListAPIView):
    queryset = WorkingPlace.objects.all()
    serializer_class = WorkingPlaceDetailSerializer
