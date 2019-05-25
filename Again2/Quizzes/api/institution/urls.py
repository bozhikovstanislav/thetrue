from django.urls import path,re_path

from .views import WorkDetailView, WorkListView

urlpatterns = [
    re_path(r'^$', WorkDetailView.as_view()),
    re_path(r'^create/$', WorkListView.as_view()),
]
