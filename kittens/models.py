from django.db import models
from django.conf import settings

class Breed(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Kitten(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    age = models.IntegerField()
    description = models.TextField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='kittens')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='kittens')

    def __str__(self):
        return self.name
