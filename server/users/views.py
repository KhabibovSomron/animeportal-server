from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response


# Create your views here.
class LoginAuthView(generics.GenericAPIView):
    """Login user"""
    def get(self, request):
        return Response(data={"message": "Hello"}, status=status.HTTP_200_OK)