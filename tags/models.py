from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(unique=True,max_length=255)
    slug = models.SlugField(unique=True,max_length=255)

