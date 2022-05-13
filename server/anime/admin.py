from django.contrib import admin
from .models import Genre, Category, Anime, Season, Episode, Film
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
