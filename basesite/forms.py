from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    """ФОРМА ОТЗЫВОВ"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text", "movie")