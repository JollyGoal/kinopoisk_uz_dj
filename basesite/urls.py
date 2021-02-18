from django.urls import path
from . import views

# from .views import TestView

urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("movie/<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
    # path('api/', TestView.as_view(), name='test')
    ]
