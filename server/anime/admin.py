from django.contrib import admin
from .models import AnimeShots, Genre, Category, Anime, Rating, RatingStar, Reviews, Season, Episode, Film
# Register your models here.

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url", "trailer")


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ("id", "anime", "number", "title", "year")


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "season", "number")

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("id", "anime", "title", 'number')

@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ("id", "value")

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "star", "anime")

@admin.register(AnimeShots)
class AnimeShotsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "anime")

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'anime', 'text']