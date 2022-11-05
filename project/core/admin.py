from django.contrib import admin
from .models import Author, Book, Review, Genre


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Genre)

# @admin.register(Book)
# class BookListAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'favorites', 'publish_date', 'average_rating')
#     search_fields = ('name', 'description','favorites')
#     list_filter = ('name', 'description', 'favorites', 'publish_date', 'average_rating')
#

# @admin.register(Author)
# class AuthorListAdmin(admin.ModelAdmin):
#     list_display = ('name', 'age')
#     search_fields = ('name', 'age')
#     list_filter = ('name', 'age')
#
#
# @admin.register(Review)
# class ReviewListAdmin(admin.ModelAdmin):
#     list_display = ('author', 'rating', 'review_text')
#     search_fields = ('author', 'rating', 'review_text')
#     list_filter = ('author', 'rating',  'review_text')
#
#
# @admin.register(Genre)
# class GenreListAdmin(admin.ModelAdmin):
#     list_display = ('name')
#     search_fields = ('name')
#     list_filter = ('name')
