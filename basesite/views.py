from django.shortcuts import render, redirect
from django.views.generic.base import View
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Movie, Actor, MovieShots
from .forms import ReviewForm
from .serializers import (
    MovieListSerializer,
    MovieDetailSerializer,
    MovieShotsSerializer,
    ReviewCreateSerializer,
    PersonListSerializer,
    PersonDetailSerializer,
    CreateRatingSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics

def get_client_ip(self, request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        return ip
    ip = request.META.get('REMOTE_ADDR')
    return ip


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 15


class AddReview(View):
    """ОТПРАВКА ОТЗЫВОВ"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        print(form)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        else:
            print("Форма не валидна")
        return redirect(movie.get_absolute_url())


class MovieListView(ListAPIView):
    """вывод список фильмов"""
    queryset = Movie.objects.filter(draft=False)
    serializer_class = MovieListSerializer
    pagination_class = LargeResultsSetPagination

    # def get(self, request):
    #     movie = Movie.objects.filter(draft=False).annotate(
    #         ratings_user=models.Case(
    #             models.When(ratings__ip=get_client_ip(self, request), then=True),
    #             default=False,
    #             output_field=models.BooleanField()
    #         )
    #     )
    #     serializer = MovieListSerializer(movie, many=True)
    #     return Response(serializer.data)


class MovieDetailView(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movie)
        movie_shots = MovieShots.objects.filter(movie__id=pk)
        ser_shots = MovieShotsSerializer(movie_shots, many=True)
        return Response({'movie': serializer.data, 'shots': ser_shots.data})

    def post(self, request, pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movie)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ReviewCreateView(generics.CreateAPIView):
    """ДОБАВЛЕНИЕ ОТЗЫВА К ФИЛЬМУ"""
    serializer_class = ReviewCreateSerializer

class PersonsListView(generics.ListAPIView):
    """ВЫВОД СПИСКА ПЕРСОН"""
    queryset = Actor.objects.all()
    serializer_class = PersonListSerializer

class PersonsDetailView(generics.RetrieveAPIView):
    """ВЫВОД ПЕРСОН"""
    queryset = Actor.objects.all()
    serializer_class = PersonDetailSerializer

class AddStarRatingView(APIView):

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=get_client_ip(request))
            return Response(status=201)
        return Response(status=400)


