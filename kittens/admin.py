from django.contrib import admin

from kittens.models import Breed, Kitten

admin.site.register(Breed)
admin.site.register(Kitten)
