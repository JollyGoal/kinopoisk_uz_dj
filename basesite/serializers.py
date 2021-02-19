from rest_framework import serializers
from .models import Movie, Genre, VideoTrailer, AgeRate, MovieShots, Reviews
from rest_framework import serializers

class MovieListserializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "original_title", "year", "url")



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

class ReviewCreateSerializers(serializers.ModelSerializer):
    """ДОБАВЛЕНИЕ ОТЗЫВА"""

    class Meta:
        model = Reviews
        fields = "__all__"

class ReviewSerializers(serializers.ModelSerializer):
    """ВЫВОД ОТЗЫВА"""

    class Meta:
        model = Reviews
        fields = ("name", "text", "parent")

class MovieDetailSerializer(serializers.ModelSerializer):
    """ПОЛНЫЙ ФИЛЬМ"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    scenario = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    genres = GenreSerializer(many=True)
    trailer = VideoSerializer()
    age_rate = AgeRateSerializer()
    reviews = ReviewSerializers(many=True)

    class Meta:
        model = Movie
        exclude = ("draft",)


class MovieShotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieShots
        fields = ('image',)

