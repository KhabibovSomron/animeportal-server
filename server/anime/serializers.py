from dataclasses import field, fields
from pyexpat import model
from statistics import mode
from rest_framework import serializers

from .models import Anime, Genre


class AnimeListSerializer(serializers.ModelSerializer):
    """список Аниме"""

    class Meta:
        model = Anime
        fields = ('title','url')