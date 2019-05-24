from kindofknowledge.models import FieldOfScience
from rest_framework import generics

from .serializer import FieldOfScienceListSerializer


class FieldOfScienceList(generics.ListCreateAPIView):
    queryset = FieldOfScience
    serializer_class = FieldOfScienceListSerializer
