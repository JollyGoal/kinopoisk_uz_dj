# Module imports
from django.contrib import admin
from django.utils.safestring import mark_safe
# Local imports
from .models import Category, Genre, MovieShots, Actor, Rating, Film, \
    RatingStar, Reviews, VideoTrailer, Director, Scenario, Serial, Cartoon, AgeRate


# Admin site display settings
class AuthorAdmin(admin.ModelAdmin):
    pass


# Model display settings

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "name")
    list_display_links = 'name',


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("title", "original_title", "id", 'display_poster', 'draft')
    save_on_top = True
    list_editable = 'draft',
    save_as = True
    fields = (('category', 'genres',),)

    def display_poster(self, obj):
        return mark_safe(f"<img src={obj.poster.url} height='25'")

    display_poster.short_description = 'Изображение'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(Cartoon)
class CartoonAdmin(admin.ModelAdmin):
    list_display = 'title',


@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    list_display = 'title',


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = 'title',


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = 'star',


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = 'value',


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(VideoTrailer)
class VideoTrailerAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(AgeRate)
class AgeRateAdmin(admin.ModelAdmin):
    list_display = 'name',
