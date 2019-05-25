from learnings.models import Quizzes, Article, Tasks
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class QuizzesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = '__all__'


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
