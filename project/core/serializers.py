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
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['name', 'favorites', 'average_rating', 'author', 'genres']


    def create(self, validated_data):
        author_data = validated_data.pop('author')
        genres_data = validated_data.pop('genres')

        # genre = Genre.objects.bulk_create(genres_data)
        book = Book.objects.create(**validated_data)
        # Author.objects.create(name=author_data, **author_data)
        # Genre.objects.create(name=genres_data, **genres_data)
        # book.genres = Genre.objects.filter(name=genres_data[0]["name"])
        # book.save()


        return super().create(**validated_data)


class BookDetailSerializer(BookListSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta(BookListSerializer.Meta):
        model = Book
        fields = BookListSerializer.Meta.fields + ['description', 'publish_date', 'reviews']

    # def create(self, validated_data):
    #     reviews_data = validated_data.pop('reviews')
    #     book = Book.objects.create(**validated_data)
    #     Review.objects.create(author=reviews_data, **reviews_data)
    #     return book


