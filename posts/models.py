from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    #tytuł o max. długości 255 znaków
    title = models.CharField(max_length=255)

    #pole tekstowe o nieokreślonej długości
    content = models.TextField()

    #flaga true/false
    published = models.BooleanField(default=False)

    #data publikacji
    created = models.DateTimeField(auto_now_add=True)

    #data ostatniej modyfikacji
    modified = models.DateTimeField(auto_now=True)

    #
    sponsored = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} {self.title}'