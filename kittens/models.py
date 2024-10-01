from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


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

class Rating(models.Model):
    kitten = models.ForeignKey('Kitten', on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Оценка должна быть от 1 до 5"
    )

    class Meta:
        unique_together = ('kitten', 'user')

    def __str__(self):
        return f"Rating {self.score} for {self.kitten.name} by {self.user.email}"
