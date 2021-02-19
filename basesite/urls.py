from django.urls import path
from . import views

# from .views import MovieListserializer, MovieDetailSerializer

urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("movie/<slug:slug>/", views.MovieDetailsView.as_view(), name="movie_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
    path("movies/", views.MovieListView.as_view()),
    path("movies/<int:pk>/", views.MovieDetailView.as_view()),
    # path("movies/shots", views.MovieShotsView.as_view()),
    ]
