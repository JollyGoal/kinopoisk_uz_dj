from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie, Actor
from .forms import ReviewForm
from .serializers import MovieListserializer, MovieDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class MoviesView(ListView):
    """СПИСОК ФИЛЬМОВ"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movies_list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context

class MovieDetailsView(DetailView):
    """ПОЛНОЕ ОПИСАНИЕ ФИЛЬМА"""
    model = Movie
    slug_field = "url"



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

class ActorView(DetailView):
    """ВЫВОД ИНФОРМАЦИИ О АКТЕРЕ"""
    model = Actor
    template_name = 'basesite/actor.html'
    slug_field = "name"



class MovieListView(APIView):

    """вывод список фильмов"""

    def get(self, request):
        movie = Movie.objects.filter(draft=False)
        serializer = MovieListserializer(movie, many=True)
        return Response(serializer.data)

class MovieDetailView(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)


    def post(self, request, pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movie)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


