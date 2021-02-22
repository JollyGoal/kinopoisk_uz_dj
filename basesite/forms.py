from django import forms
from .models import Reviews
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
    """ФОРМА ОТЗЫВОВ"""
    class Meta:
        model = Reviews
        fields = ("author", "email", "text", "movie")
