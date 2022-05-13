from dataclasses import fields
from statistics import mode
from rest_framework import serializers

from .models import Anime, Genre

class AnimeSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    category = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    class Meta:
        model = Anime
        fields = [
            'id',
            'title',
            'description',
            'poster',
            'genres',
            'category',
            'url',
            'draft',
            'trailer'
        ]