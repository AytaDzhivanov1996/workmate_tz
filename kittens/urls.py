from rest_framework.routers import DefaultRouter
from django.urls import path, include

from kittens.views import BreedViewSet, KittenViewSet

router = DefaultRouter()
router.register(r'breeds', BreedViewSet, basename='breed')
router.register(r'kittens', KittenViewSet, basename='kitten')

urlpatterns = [
    path('', include(router.urls)),
]