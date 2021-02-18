from django import template
from basesite.models import Category, Movie


register = template.Library()


@register.simple_tag()
def get_categories():
    """ВЫВОД ВСЕХ КАТЕГОРИЙ"""
    return Category.objects.all()

@register.inclusion_tag('basesite/tags/last_movie.html')
def get_last_movies(count=5):
    movies = Movie.objects.order_by("id")[:count]
    return {"last_movies": movies}
