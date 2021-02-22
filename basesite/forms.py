from django import forms
from .models import Reviews, UserProfile
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
    """ФОРМА ОТЗЫВОВ"""
    class Meta:
        model = Reviews
        fields = ("first_name", "name", "email", "text", "movie")
