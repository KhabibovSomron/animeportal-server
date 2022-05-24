from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
class Category(models.Model):
    """Категория"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанры"
        verbose_name_plural = "Жанры"


class Anime(models.Model):
    """Аниме"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="images/anime-poster/")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    trailer = models.CharField("Трайлер", max_length=500, default="")

    def __str__(self):
        return self.title

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    # def get_absolute_url(self):
    #     return reverse("anime_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Аниме"
        verbose_name_plural = "Аниме"

class Season(models.Model):
    """Сезон"""
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name="fk_anime")
    number = models.PositiveSmallIntegerField("Номер сезона", default=0)
    year = models.PositiveSmallIntegerField("Дата выхода сезона", default=1990)
    title = models.CharField("Название сезона", max_length=300, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сезон"
        verbose_name_plural = "Сезон"

class Episode(models.Model):
    """Серия"""
    season = models.ForeignKey(Season, on_delete=models.CASCADE,verbose_name="fk_season")
    title = models.CharField("Название серий", max_length=150, null=True)
    number = models.PositiveSmallIntegerField("Номер серий", default=0)
    image = models.ImageField(upload_to="images/episode-preview/")
    file = models.FileField(
        upload_to=f"video/serials/",
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Серия"
        verbose_name_plural = "Серия"


class Film(models.Model):
    """Полнометражное Аниме"""
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE,verbose_name="fkf_anime")
    title = models.CharField("Название фильма", max_length=150, null=True)
    number = models.PositiveSmallIntegerField("Номер фильма", default=0)
    image = models.ImageField(upload_to="images/episode-preview/")
    file = models.FileField(
        upload_to=f"video/films/",
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильм"


class AnimeShots(models.Model):
    """Кадры из аниме"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="anime_shots/")
    anime = models.ForeignKey(Anime, verbose_name="Аниме", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадры из аниме"
        verbose_name_plural = "Кадры из аниме"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f"{self.value}"

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезда рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name="аниме")

    def __str__(self):
        return f"{self.star} - {self.anime}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинг"

