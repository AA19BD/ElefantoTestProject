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
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Book
        fields = ['name', 'favorites', 'average_rating', 'author', 'genres']

    def create(self, validated_data):
        author = Author.objects.get(name=validated_data["author"]["name"])
        genre_id = Genre.objects.get(name=validated_data["genres"][0]["name"]).id
        review_id = Review.objects.create(author=validated_data["reviews"][0]["author"],
                                          rating=validated_data["reviews"][0]["rating"],
                                          review_text=validated_data["reviews"][0]["review_text"]).id

        book = Book.objects.create(name=validated_data["name"],
                                   description=validated_data["description"],
                                   author=author,
                                   )

        book.genres.set(objs=[genre_id])
        book.reviews.set(objs=[review_id])
        return book


class BookDetailSerializer(BookListSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta(BookListSerializer.Meta):
        model = Book
        fields = BookListSerializer.Meta.fields + ['description', 'publish_date', 'reviews']



