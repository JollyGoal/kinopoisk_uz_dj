from rest_framework import serializers
from .models import Movie, Genre, VideoTrailer, AgeRate, MovieShots


class MovieListserializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "tagline", "category")



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name", "url")


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoTrailer
        fields = "__all__"


class AgeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeRate
        fields = "__all__"


class MovieDetailSerializer(serializers.ModelSerializer):
    """ПОЛНЫЙ ФИЛЬМ"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    scenario = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    genres = GenreSerializer(many=True)
    trailer = VideoSerializer()
    age_rate = AgeRateSerializer()

    class Meta:
        model = Movie
        exclude = ("draft",)


class MovieShotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieShots
        fields = ('image',)
