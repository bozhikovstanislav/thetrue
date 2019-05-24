from django.contrib import admin
from django.urls import path,include
from .views import ProfessionListView

urlpatterns = [
    path('',ProfessionListView.as_view())
]
