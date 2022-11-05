import sys
import os

from django.db import models
from utils.constants import GENRE_TYPE, GENRE_TYPE_POETRY


sys.path.append(os.getcwd())


class Author(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    age = models.IntegerField(default=0, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f'name: {self.name}, age: {self.age}'


class Genre(models.Model):
    name = models.CharField(choices=GENRE_TYPE, default=GENRE_TYPE_POETRY, max_length=250, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return f'name: {self.name}'


class Review(models.Model):
    author = models.CharField(max_length=250, null=True, blank=True)
    rating = models.IntegerField(default=0, blank=True)
    review_text = models.TextField(blank=True)

    class Meta:
        ordering = ['author']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'author: {self.author}, rating: {self.rating}'


class Book(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    favorites = models.BooleanField(default=False, blank=True)
    publish_date = models.DateField(auto_now_add=True)
    average_rating = models.FloatField(default=0, null=True, blank=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', blank=True)
    genres = models.ManyToManyField(Genre, related_name='books', blank=True)
    reviews = models.ManyToManyField(Review, related_name='books', blank=True)


    class Meta:
        ordering = ['publish_date']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return f'name: {self.name}, publish_date: {self.publish_date}'














