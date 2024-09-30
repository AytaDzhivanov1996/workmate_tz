from rest_framework import serializers

from kittens.models import Kitten, Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'

class KittenSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.name')

    class Meta:
        model = Kitten
        fields = '__all__'
