from rest_framework.routers import DefaultRouter
from django.urls import path, include

from kittens.views import BreedViewSet, KittenViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'breeds', BreedViewSet, basename='breed')
router.register(r'kittens', KittenViewSet, basename='kitten')
router.register(r'ratings', RatingViewSet, basename='rating')

urlpatterns = [
    path('', include(router.urls)),
]