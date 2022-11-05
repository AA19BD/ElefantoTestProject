from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, GenreViewSet, AuthorViewSet, ReviewViewSet


router = routers.SimpleRouter()
router.register(r'book',BookViewSet)
router.register(r'genre',GenreViewSet)
router.register(r'author',AuthorViewSet)
router.register(r'review',ReviewViewSet)


# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls))
]
