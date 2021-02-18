from django.db import models
from datetime import date
from django.urls import reverse


class Category(models.Model):
    """КАТЕГОРИИ"""
    name = models.CharField("Категории", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class AgeRate(models.Model):
    """ВОЗРАСТНОЙ РЕЙТИНГ"""
    name = models.CharField("Возрастной рейтинг", max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Возрастной рейтинг"
        verbose_name_plural = "Возрастные рейтинги"


class Actor(models.Model):
    """Актеры """
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актеры"
        verbose_name_plural = "Актеры"


# class Director(models.Model):
#     """Директоры """
#     name = models.CharField("Имя", max_length=100)
#     age = models.PositiveSmallIntegerField("Возраст", default=0)
#     description = models.TextField("Описание")
#     image = models.ImageField("Изображение", upload_to="actors/")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "Режиссер"
#         verbose_name_plural = "Режиссеры"
#
# class Scenario(models.Model):
#     """Сценаристы """
#     name = models.CharField("Имя", max_length=100)
#     age = models.PositiveSmallIntegerField("Возраст", default=0)
#     description = models.TextField("Описание")
#     image = models.ImageField("Изображение", upload_to="actors/")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "Сценарист"
#         verbose_name_plural = "Сценаристы"


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class VideoTrailer(models.Model):
    """ТРЕЙЛЕР"""
    name = models.CharField("Название трейлера", max_length=100)
    file = models.FileField("Видео", upload_to="trailers/", null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Трейлер"
        verbose_name_plural = "Трейлеры"


class Movie(models.Model):
    """Фильм"""
    title = models.CharField("Название", max_length=100)
    original_title = models.CharField("Оригинальное название фильма", max_length=100, blank=True)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2021)
    country = models.CharField("Страна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="Режиссер",
                                       related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Актеры",
                                    related_name="film_actor")
    # scenario = models.ManyToManyField(Scenario, verbose_name="Сценаристы",
    #                                 related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    world_premiere = models.DateField("Премьера в мире", default=date.today)
    category = models.ForeignKey(Category, verbose_name="Категория",
                                 on_delete=models.SET_NULL, null=True)
    duration = models.CharField("Продолжиетельность", max_length=100, blank=False)
    age_rate = models.ForeignKey(AgeRate, verbose_name="Возрастной рейтинг", on_delete=models.CASCADE)
    trailer = models.ForeignKey(VideoTrailer, verbose_name="Трейлер", on_delete=models.CASCADE)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.original_title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Serial(Movie):
    episod = models.PositiveSmallIntegerField("Количество Эпизодов", null=False)
    season = models.PositiveSmallIntegerField("Количество сезонов", null=False)

    def __str__(self):
        return self.original_title

    class Meta:
        verbose_name = "Сериал"
        verbose_name_plural = "Сериалы"


class Film(Movie):
    budget = models.PositiveSmallIntegerField("Бюджет", default=0,
                                              help_text="укажите сумму в долларах")
    fees_in_world = models.PositiveIntegerField("Сборы в мире", default=0,
                                                help_text="укажите сумму в долларах")

    def __str__(self):
        return self.original_title

    class Meta:
        verbose_name = "Фильмы"
        verbose_name_plural = "Фильмы"


class Cartoon(Movie):
    budget = models.PositiveSmallIntegerField("Бюджет", default=0,
                                              help_text="укажите сумму в долларах")
    fees_in_world = models.PositiveIntegerField("Сборы в мире", default=0,
                                                help_text="укажите сумму в долларах")

    def __str__(self):
        return self.original_title

    class Meta:
        verbose_name = "Мультфильм"
        verbose_name_plural = "Мультфильмы"


class MovieShots(models.Model):
    """КАДРЫ ИЗ ФИЛЬМА"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"


class RatingStar(models.Model):
    """ЗВЕЗДА РЕЙТИНГА"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    """РЕЙТИНГ"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """ОТЗЫВ"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель",
                               on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
