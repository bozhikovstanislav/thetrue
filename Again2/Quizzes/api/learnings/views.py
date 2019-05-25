from rest_framework import generics
from .serializers import ArticleSerializer,QuizzesSerializer,TasksSerializer
from learnings.models import Article,Tasks,Quizzes


class ArticleAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class TasksAPIView(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class QuizzesAPIView(generics.ListCreateAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizzesSerializer
