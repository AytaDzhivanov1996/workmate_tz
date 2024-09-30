from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from kittens.models import Breed, Kitten
from kittens.serializers import BreedSerializer, KittenSerializer


class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [AllowAny]


class KittenViewSet(viewsets.ModelViewSet):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        breed_id = self.request.query_params.get('breed')
        if breed_id:
            return Kitten.objects.filter(breed_id=breed_id)
        return Kitten.objects.all()
    
    def perform_update(self, serializer):
        kitten = self.get_object()
        if kitten.owner != self.request.user:
            raise PermissionError('You cannot update this kitten')
        serializer.save()
    
    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionError('You cannot delete this kitten')
        instance.delete()