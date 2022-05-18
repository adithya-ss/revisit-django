from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)        # Unique as True will act similar to a primary key. But not a PK.
    description = models.TextField()            # TextField is used to store larger data than CharField
    image = models.ImageField(upload_to='images')                 # Stores a reference to the path of the file. Does not actually store the image.