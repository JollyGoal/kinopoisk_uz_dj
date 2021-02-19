from django.urls import path
from . import views

urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("movies/", views.MovieListView.as_view()),
    path("movies/<int:pk>/", views.MovieDetailView.as_view()),
    path("review/", views.ReviewCreateView.as_view()),

]
