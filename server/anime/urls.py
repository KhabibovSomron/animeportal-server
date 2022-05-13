from django.urls import path

from . import views

urlpatterns = [
    path('<slug:url>/', views.AnimeDetailAPIView.as_view(), name="anime_detail")
]
