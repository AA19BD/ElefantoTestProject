from rest_framework import serializers
from .models import Author, Book, Genre, Review


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'favorites', 'average_rating','author', 'genres']


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


