from djoser.conf import User
from rest_framework import serializers
from .models import Movie, Genre, VideoTrailer, AgeRate, MovieShots, Reviews, Actor, Rating, UserProfile, User
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

class PersonListSerializer(serializers.ModelSerializer):
    """ВЫВОД СПИСОК АКТЕРОВ РЕЖИССЕРОВ И СЦЕНАРИСТОВ"""
    class Meta:
        model = Actor
        fields = ("id", "name", "image", "url", )


class PersonDetailSerializer(serializers.ModelSerializer):
    """ВЫВОД ИНФОРМАЦИИ АКТЕРОВ РЕЖИССЕРОВ И СЦЕНАРИСТОВ"""
    class Meta:
        model = Actor
        fields = "__all__"


class MovieListSerializer(serializers.ModelSerializer):
    # ratings_user = serializers.BooleanField()

    class Meta:
        model = Movie
        fields = ("title", "tagline", "category", "ratings")


class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("star", "movie")

    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            movie=validated_data.get('movie', None),
            defaults={'star': validated_data.get('star')}
        )
        return rating


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'




    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            movie=validated_data.get('movie', None),
            defaults={'star': validated_data.get('star')}
        )
        return rating




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
    directors = PersonListSerializer(many=True)
    actors = PersonListSerializer(many=True)
    scenario = PersonListSerializer(many=True)
    genres = GenreSerializer(many=True)
    trailer = VideoSerializer()
    age_rate = AgeRateSerializer()
    reviews = ReviewSerializer(many=True)
    ratings = CreateRatingSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ("draft",)


class MovieShotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieShots
        fields = ('image',)



