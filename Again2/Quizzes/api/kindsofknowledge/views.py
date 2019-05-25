from kindsofknowledge.models import FieldOfScience
from rest_framework import generics
from .serializers import FieldOfScienceListSerializer


class FieldOfScienceView(generics.ListCreateAPIView):
    serializer_class = FieldOfScienceListSerializer

    def get_queryset(self):
        querieset=FieldOfScience.objects.all()
        return querieset



class DetailFieldOfScienceView():
    pass
