from rest_framework import viewsets
from .models import Author, Book, Review, Genre
from .serializers import BookListSerializer, BookDetailSerializer, AuthorSerializer, GenreSerializer, ReviewSerializer
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from django_filters import rest_framework as filters
from .filters import BookFilter


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    parser_classes = (FormParser, MultiPartParser, JSONParser)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter

    def get_serializer_class(self):
        if self.action == 'list':
            serializer_class = BookListSerializer
        else:
            serializer_class = BookDetailSerializer
        return serializer_class


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    parser_classes = (FormParser, MultiPartParser, JSONParser)
    serializer_class = GenreSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    parser_classes = (FormParser, MultiPartParser, JSONParser)
    serializer_class = AuthorSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    parser_classes = (FormParser, MultiPartParser, JSONParser)
    serializer_class = ReviewSerializer

