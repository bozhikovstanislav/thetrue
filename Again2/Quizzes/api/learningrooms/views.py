from rest_framework import generics

from learningrooms.models import RoomQuizze
from .serializers import RoomQuizzesSerilizer


class QuizzesAPIView(generics.ListCreateAPIView):
    queryset = RoomQuizze
    serializer_class = RoomQuizzesSerilizer
