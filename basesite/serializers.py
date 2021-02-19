from rest_framework import serializers
from .models import Movie, Genre, VideoTrailer, AgeRate, MovieShots, Reviews
from rest_framework import serializers


class FilterReviewListSerializer(serializers.ListSerializer):
    """ФИЛЬТР КОММЕНТАРИЕВ, ТОЛЬКО PARENTS"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)

class RecursiveSerializer(serializers.ModelSerializer):
    """ВЫВОД РЕКУРСИВНО CHILDREN"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class MovieListSerializer(serializers.ModelSerializer):

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

class ReviewCreateSerializer(serializers.ModelSerializer):
    """ДОБАВЛЕНИЕ ОТЗЫВА"""

    class Meta:
        model = Reviews
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    """ВЫВОД ОТЗЫВА"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Reviews
        fields = ("name", "text", "children")

class MovieDetailSerializer(serializers.ModelSerializer):
    """ПОЛНЫЙ ФИЛЬМ"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    scenario = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    genres = GenreSerializer(many=True)
    trailer = VideoSerializer()
    age_rate = AgeRateSerializer()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ("draft",)


class MovieShotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieShots
        fields = ('image',)



