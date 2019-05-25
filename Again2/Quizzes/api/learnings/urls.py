from django.urls import path

from . import views

urlpatterns = [
    path(r'article/', views.ArticleAPIView.as_view(), name="article-list"),
    path(r'quizzes/', views.QuizzesAPIView.as_view(), name="quizzes-list"),
    path(r'tasks/', views.TasksAPIView.as_view(), name="tasks-list"),

]
