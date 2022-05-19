from distutils.command.upload import upload
from operator import mod
from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=350)

    def __str__(self):
        return f'{self.name} - {self.address}'

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)            # Unique as True will act similar to a primary key. But not a PK.
    description = models.TextField()                # TextField is used to store larger data than CharField
    image = models.ImageField(upload_to='images')   # Stores a reference to the path of the file. Does not actually store the image.
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} : {self.slug}'
