from django import forms
from .models import Reviews
# from customusers.models import Account


class ReviewForm(forms.ModelForm):
    """ФОРМА ОТЗЫВОВ"""
    class Meta:
        model = Reviews
        fields = ("author",  "text", "movie")
