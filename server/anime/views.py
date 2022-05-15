from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import AnimeListSerializer
from .models import Anime, Genre


# Create your views here.
class AnimeListView(APIView):
    """Вывод списка аниме"""
    def get(self, request):
        anime = Anime.objects.filter(draft=False)
        serializer = AnimeListSerializer(anime, many=True)
        return Response(serializer.data)