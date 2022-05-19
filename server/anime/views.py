from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from itertools import groupby

from .serializers import AllGenresSerializer, AnimeDetailSerializer, AnimeListSerializer, EpisodeSerializer, SeasonYearSerializer
from .models import Anime, Episode, Genre, Season


# Create your views here.
class AnimeListView(APIView):
    """Вывод списка аниме"""
    def get(self, request):
        anime = Anime.objects.filter(draft=False)
        serializer = AnimeListSerializer(anime, many=True)
        return Response(serializer.data)


class GetAllGenresView(APIView):
    """Вывод жанров"""

    def get(self, request):
        genres = Genre.objects.all()
        serializer = AllGenresSerializer(genres, many=True)
        return Response(serializer.data)


class GetAllYearsView(APIView):
    """Вывод года выхода аниме"""

    def get(self, request):
        years = Season.objects.all().values('year')
        serializer = SeasonYearSerializer(years, many=True)
        return Response(serializer.data)

class GetAnimePosterView(APIView):

    def get(self, request):
        poster = Anime.objects.all()
        serializer = GetAnimePosterView(poster, many=True)
        return Response(serializer.data)


class GetAnimeDetailView(APIView):
    
    def get(self, request, pk):
        anime = Anime.objects.get(id=pk, draft=False)
        serializer = AnimeDetailSerializer(anime)
        return Response(serializer.data)


class GetEpisodeView(APIView):
    
    def get(self, request, pk):
        episode = Episode.objects.get(id=pk)
        serializer = EpisodeSerializer(episode)
        return Response(serializer.data)


class GetAnimeFilterView(APIView):
    def get(self, request):
        if self.request.GET.getlist("genres"):
            anime = Anime.objects.filter(genres__in=self.request.GET.getlist("genres"), draft=False).distinct()
        else:
            anime = Anime.objects.filter(draft=False)
        serializer = AnimeListSerializer(anime, many=True)
        return Response(serializer.data)


class SearchAnimeView(APIView):
    def get(self, request):
        anime = Anime.objects.filter(title__icontains=self.request.GET.get("title"), draft=False)
        serializer = AnimeListSerializer(anime, many=True)
        return Response(serializer.data)