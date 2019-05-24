from .views import WorkingDetailView

from django.urls import path

urlpatterns = [
    path('',WorkingDetailView.as_view()),
]
