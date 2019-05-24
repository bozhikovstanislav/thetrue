from django.contrib import admin
from django.urls import path,include
from .views import FieldOfScienceList

urlpatterns = [
    path('',FieldOfScienceList.as_view())
]
