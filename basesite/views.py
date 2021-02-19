from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Movie, Actor, MovieShots
from .forms import ReviewForm
from .serializers import MovieListserializer, MovieDetailSerializer, MovieShotsSerializer, ReviewCreateSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 15


class MoviesView(ListView):
    """СПИСОК ФИЛЬМОВ"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movies_list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context


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
    serializer_class = MovieListserializer
    pagination_class = LargeResultsSetPagination


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

class ReviewCreateView(APIView):
    """ДОБАВЛЕНИЕ ОТЗЫВА К ФИЛЬМУ"""

    def post(self, request):
        review = ReviewCreateSerializers(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)