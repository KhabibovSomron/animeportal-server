from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginAuthView.as_view(), name="login"),
]
