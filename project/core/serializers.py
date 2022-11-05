from rest_framework import serializers
from .models import Author, Book, Genre, Review


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['name', 'favorites', 'average_rating', 'author', 'genres']


class BookDetailSerializer(BookListSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta(BookListSerializer.Meta):
        model = Book
        fields = BookListSerializer.Meta.fields + ['description', 'publish_date', 'reviews']

    # def create(self, validated_data):
    #     return Review.objects.create(author=,rating=,review_text=)



