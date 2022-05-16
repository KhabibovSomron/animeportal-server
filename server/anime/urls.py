from django.urls import path

from . import views

urlpatterns = [
    path('animelist/', views.AnimeListView.as_view()),
    path('genres/', views.GetAllGenresView.as_view()),
    path('years/', views.GetAllYearsView.as_view()),
    path('anime-detail/<int:pk>/', views.GetAnimeDetailView.as_view())
]
