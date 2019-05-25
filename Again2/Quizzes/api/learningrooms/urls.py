from django.contrib import admin
from django.urls import path,include,re_path
#from django.contrib.auth.views import logout

from .views import QuizzesAPIView
from accounts.views import (login_view, register_view,logout_view)


urlpatterns = [
    path('',QuizzesAPIView.as_view()),

    #re_path(r'^logout/$', logout, {'next_page': '/login/'}, name='logout'),

]