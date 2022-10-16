from django.db import models

# Create your models here.
class Book(models.Model):
    #tytuł książki
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    description = models.TextField()
    available = models.BooleanField()
    publication_year = models.IntegerField()

    def __str__(self):
        return f'{self.title}: {self.author}'