# Module imports
from django.contrib import admin
from django.utils.safestring import mark_safe
# Local imports
from .models import Category, Genre, MovieShots, Actor, Rating, \
    RatingStar, Reviews, VideoTrailer, AgeRate, Movie


# Admin site display settings
class AuthorAdmin(admin.ModelAdmin):
    pass


# Model display settings

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "name")
    list_display_links = 'name',

class MovieShotsInLine(admin.StackedInline):
    model = MovieShots
    extra = 3
    fields = (('image', "display_screenshots"),)
    readonly_fields = ("display_screenshots",)

    def display_screenshots(self, obj):
        return mark_safe(f"<img src={obj.image.url} height='400'")

    display_screenshots.short_description = 'Скриншот'


@admin.register(Movie)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("title", "original_title", "id", 'draft')
    save_on_top = True
    list_editable = 'draft',
    save_as = True
    fieldsets = [
        (None, {'fields': ['title', 'original_title', 'year', 'country', 'category']}),
        ('Информация', {'fields': ['tagline', 'description', 'genres']}),
        ('Команда', {'fields': ['actors', 'scenario', 'director', ]}),
        ('Информация для фильма', {'fields': ['budget', 'fees_in_world']}),
        ('Информация для сериала', {'fields': ['episode', 'seasons']}),
        ('XZ', {'fields': ['world_premiere', 'duration', 'age_rate']}),
        ('Постер', {'fields': [('poster', 'display_poster')]}),

    ]
    readonly_fields = ("display_poster",)
    inlines = [MovieShotsInLine]

    def display_poster(self, obj):
        return mark_safe(f"<img src={obj.poster.url} height='400'")

    display_poster.short_description = 'Постер'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = 'name',


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


# @admin.register(Director)
# class DirectorAdmin(admin.ModelAdmin):
#     list_display = 'name',
#
#
# @admin.register(Scenario)
# class ScenarioAdmin(admin.ModelAdmin):
#     list_display = 'name',


@admin.register(AgeRate)
class AgeRateAdmin(admin.ModelAdmin):
    list_display = 'name',
