# Module imports
from django.contrib import admin
from django.utils.safestring import mark_safe
# Local imports
from .models import Category, Genre, Actor, Rating, MovieShots, RatingStar, Reviews, VideoTrailer, AgeRate, Movie, Director, Scenario


# Admin site display settings
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.site_title = "Кинопоиск уз"
admin.site.site_header = "Кинопоиск уз"

# Model display settings

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "name")
    list_display_links = 'name',



    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"

# @admin.register(MovieShots)
# class MovieShotsAdmin(admin.ModelAdmin):
#     """КАДРЫ ИЗ ФИЛЬМА"""
#     list_display = 'image',
#     readonly_fields = 'get_image',
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.image.url} width="50" height="60"')
#
#     get_image.short_description = "Изображение"

class MovieShotsInLine(admin.TabularInline):
    model = MovieShots
    extra = 1

    fields = (('image', "display_screenshots"),)
    readonly_fields = ("display_screenshots",)

    def display_screenshots(self, obj):
        return mark_safe(f"<img src={obj.image.url} height='400'")

    display_screenshots.short_description = 'Скриншот'

class ReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("author", )

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "original_title", "category", "id", 'draft'    )
    list_filter = ("category", "year")
    save_on_top = True
    list_editable = 'draft',
    save_as = True
    fieldsets = [
        (None, {'fields': ['title', 'original_title', 'year', 'country', 'category']}),
        ('Информация', {'fields': ['tagline', 'description', 'genres']}),
        ('Команда', {'fields': ['actors', 'scenario', 'directors', ]}),
        ('Информация для фильма', {'fields': ['budget', 'fees_in_world']}),
        ('Информация для сериала', {'fields': ['episode', 'seasons']}),
        ('Дополнительно', {'fields': ['world_premiere', 'duration', 'age_rate']}),
        ('Постер', {'fields': [('poster', 'display_poster')]}),
        ('Трейлер', {'fields': ['trailer']}),

    ]
    # def display_file(self, obj):
    #     return mark_safe(f"<img src={obj.trailer.url}")
    #
    # display_file.short_description = 'Трейлер'

    readonly_fields = ("display_poster",)
    inlines = [MovieShotsInLine, ReviewInLine]

    def display_poster(self, obj):
        return mark_safe(f"<img src={obj.poster.url} height='400'")

    display_poster.short_description = 'Постер'

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author", "parent", "movie", "id", )
    readonly_fields = ("author", "date")

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = 'name',


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = 'name', 'image'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = 'star',


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = 'value',





@admin.register(VideoTrailer)
class VideoTrailerAdmin(admin.ModelAdmin):
    list_display = 'name', 'file'
    readonly_fields = 'get_file',

    def get_file(self, obj):
        return mark_safe(f'<img src={obj.file.url} width="500" height="600"')

    get_file.short_description = "Трейлер"

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(AgeRate)
class AgeRateAdmin(admin.ModelAdmin):
    list_display = 'name',
