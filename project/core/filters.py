from django_filters import rest_framework as filters
from .models import Book


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class BookFilter(filters.FilterSet):
    genres = CharFilterInFilter(field_name="genres__name", lookup_expr='in')
    author = CharFilterInFilter(field_name="author__name", lookup_expr='in')
    publish_date = filters.DateFromToRangeFilter()

    class Meta:
        model = Book
        fields = ['genres','author','publish_date']
