from professions.models import Profession
from rest_framework.generics import ListCreateAPIView

from .serializer import ProfessionListSerializer


class ProfessionListView(ListCreateAPIView):
    queryset = Profession
    serializer_class = ProfessionListSerializer
