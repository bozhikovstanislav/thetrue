from django.conf.urls import re_path
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserLoginAPIView
    )

urlpatterns = [
    re_path(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    re_path(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    re_path(r'^profile/$', UserCreateAPIView.as_view(), name='register'),
]



