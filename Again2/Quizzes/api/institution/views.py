from institution.models import WorkingPlace
from rest_framework import generics

from .serializers import WorkingPlaceDetailSerializer


class WorkDetailView(generics.ListAPIView):
    queryset = WorkingPlace.objects.all()
    serializer_class = WorkingPlaceDetailSerializer


class WorkListView(generics.ListCreateAPIView):
    serializer_class = WorkingPlaceDetailSerializer

    def get_queryset(self):
        queriset = WorkingPlace.objects.All()
        return queriset