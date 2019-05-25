from professions.models import Profession
from rest_framework import generics

from .serializers import ProfessionSerializer


class ProfessionListView(generics.ListCreateAPIView):
    serializer_class = ProfessionSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category is not None:
            queriset = Profession.objects.filter(category=category)
            return queriset
        queriset = Profession.objects.all()
        return queriset
