from django.urls import path

from . import views

urlpatterns = [
    path('animelist/', views.AnimeListView.as_view())
]
