from django.contrib import admin
from .models import Category, Genre, Film, MovieShots, Actor, Rating, RatingStar, Reviews, VideoTrailer, Serial, Cartoon, AgeRate

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Film)
admin.site.register(Serial)
admin.site.register(Cartoon)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
admin.site.register(VideoTrailer)
# admin.site.register(Director)
# admin.site.register(Scenario)
admin.site.register(AgeRate)
