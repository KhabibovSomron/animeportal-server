import base64
from dataclasses import fields
from msilib.schema import File
from rest_framework import serializers

from .models import Anime, AnimeShots, Category, Film, Genre, RatingStar, Reviews, Season, Episode


class AnimeListSerializer(serializers.ModelSerializer):
    """список Аниме"""

    class Meta:
        model = Anime
        fields = ('id','title','url', 'poster')


class AllGenresSerializer(serializers.ModelSerializer):
    """Список жанров"""

    class Meta:
        model = Genre
        fields = ("id","name", "url")


class SeasonYearSerializer(serializers.ModelSerializer):
    """года выхода аниме"""

    class Meta:
        model = Season
        fields = ('year',)


class AnimePosterSerializer(serializers.ModelSerializer):
    """Постер"""
    base64_image = serializers.SerializerMethodField()

    class Meta:
        model = Anime
        fields = ('base64_image', 'id')

    def get_base64_image(self, obj):
        f = open(obj.poster.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        return data


class EpisodeSerializer(serializers.ModelSerializer):
    """Серия"""

    class Meta:
        model = Episode
        exclude = ('season',)


class SeasonSerializer(serializers.ModelSerializer):
    """Сезоны"""
    episodes = serializers.SerializerMethodField()

    class Meta:
        model = Season
        exclude = ('anime',)

    def get_episodes(seld, obj):
        episode = Episode.objects.filter(season=obj.id)
        serializer = EpisodeSerializer(episode, many=True)
        return (serializer.data)


class AnimeDetailSerializer(serializers.ModelSerializer):
    """Детальное описание Аниме"""
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    seasons = serializers.SerializerMethodField()

    class Meta:
        model = Anime
        exclude = ('draft', 'category')

    def get_seasons(self, obj):
        season = Season.objects.filter(anime=obj.id)
        serializer = SeasonSerializer(season, many=True)
        return (serializer.data)    


class RatingStarSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingStar
        fields = ('id', 'value')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "url")

class AnimeShotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeShots
        fields = ('id', 'title', 'image')

class AnimeFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title', 'number', 'image', 'duration', 'file')


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'


class FilterReviewListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class GetReviewsSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Reviews
        fields = ('id', 'name', 'children', 'text')