from django.urls import path

from . import views

urlpatterns = [
    path('animelist/', views.AnimeListView.as_view()),
    path('genres/', views.GetAllGenresView.as_view()),
    path('years/', views.GetAllYearsView.as_view()),
    path('anime-detail/<int:pk>/', views.GetAnimeDetailView.as_view()),
    path('episode/<int:pk>/', views.GetEpisodeView.as_view()),
    path('filter/', views.GetAnimeFilterView.as_view()),
    path('search/', views.SearchAnimeView.as_view()),
    path('rating-star/', views.GetRatingStarView.as_view()),
    path('categories/', views.GetCategoriesView.as_view()),
    path('anime-shots/<int:pk>/', views.GetAnimeShotsView.as_view())
]
