from rest_framework import serializers
from django.db import models

from kittens.models import Kitten, Breed, Rating

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'

class KittenSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Kitten
        fields = ['id', 'name', 'color', 'age', 'description', 'breed', 'owner', 'average_rating']
        
    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings.exists():
            return round(ratings.aggregate(models.Avg('score'))['score__avg'], 2)
        return None

class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Rating
        fields = '__all__'

