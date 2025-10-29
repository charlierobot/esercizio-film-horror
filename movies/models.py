
# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    poster_url = models.URLField()

    def __str__(self):
        return self.title
    
    