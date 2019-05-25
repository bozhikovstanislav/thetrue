from kindofknowledge.models import FieldOfScience
from rest_framework import status
from rest_framework.response import Response
from rest_framework import views, generics, response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import FieldOfScienceListSerializer


class FieldOfScienceView(generics.ListCreateAPIView):
    serializer_class = FieldOfScienceListSerializer

    def get_queryset(self):
        querieset=FieldOfScience.objects.all()
        return querieset



class DetailFieldOfScienceView():
    pass
