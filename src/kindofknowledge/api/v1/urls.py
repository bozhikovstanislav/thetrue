from django.contrib import admin
from django.urls import path,include
from .views import FieldOfScienceView,DetailFieldOfScienceView

urlpatterns = [
    path('',FieldOfScienceView.as_view())
]
