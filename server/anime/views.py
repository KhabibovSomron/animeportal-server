from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import AllGenresSerializer, AnimeDetailSerializer, AnimeFilmSerializer, AnimeListSerializer, AnimeShotsSerializer, CategorySerializer, EpisodeSerializer, FilmSerializer, GetReviewsSerializer, RatingStarSerializer, ReviewCreateSerializer, SeasonYearSerializer
from .models import Anime, AnimeShots, Category, Episode, Genre, Reviews, Season, RatingStar, Film


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


class GetFilmView(APIView):
    
    def get(self, request, pk):
        film = Film.objects.get(id=pk)
        serializer = FilmSerializer(film)
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


class GetRatingStarView(generics.ListAPIView):
    queryset = RatingStar.objects.all()
    serializer_class = RatingStarSerializer


class GetCategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class GetAnimeShotsView(APIView):
    def get(self, request, pk):
       shots = AnimeShots.objects.filter(anime=pk)
       serializer = AnimeShotsSerializer(shots, many=True)
       return Response(serializer.data)

class GetAnimeFilms(APIView):
    def get(self, request, pk):
       films = Film.objects.filter(anime=pk)
       serializer = AnimeFilmSerializer(films, many=True)
       return Response(serializer.data)


class ReviewCreateView(APIView):
    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)


class GetAllReviews(APIView):
    def get(self, request, pk):
        reviews = Reviews.objects.filter(anime=pk)
        serializer = GetReviewsSerializer(reviews, many=True)
        return Response(serializer.data)
        