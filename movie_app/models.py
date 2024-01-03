from django.db import models
from django.core.validators import RegexValidator

# alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$')


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    url = models.URLField(blank=True)
    iframe = models.CharField(max_length=250, blank=True)

    
class Note(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name