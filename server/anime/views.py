from cgitb import lookup
from rest_framework import generics
from rest_framework.response import Response

from .models import Anime
from .serializers import AnimeSerializer


# Create your views here.
class AnimeDetailAPIView(generics.RetrieveAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    lookup_field = 'url'