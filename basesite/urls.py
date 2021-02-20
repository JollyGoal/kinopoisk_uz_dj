from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserProfileListCreateView

urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("movies/", views.MovieListView.as_view()),
    path("movies/<int:pk>/", views.MovieDetailView.as_view()),
    path("review/", views.ReviewCreateView.as_view()),
    path("person/", views.PersonsListView.as_view()),
    path("person/<int:pk>/", views.PersonsDetailView.as_view()),
    path("ratings/", views.AddStarRatingView.as_view()),
    path("all-profiles", views.UserProfileListCreateView.as_view(),name="all-profiles"),
    path("profile/<int:pk>", views.UserProfileDetailView.as_view(), name="profile"),
    path("create/", views.UserCreateView.as_view())
]
