from django.urls import path
from . import views
from .views import TestView

urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("movie/<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path('api/', TestView.as_view(), name='test')
    ]
