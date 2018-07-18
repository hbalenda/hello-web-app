from django.db import models

# Create models
class Event(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  slug = models.SlugField(unique=True)

class Location(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  slug = models.SlugField(unique=True)
