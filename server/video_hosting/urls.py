from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.get_streaming_video, name='stream'),
]