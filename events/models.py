from django.db import models
from django.contrib.auth.models import User

# Create models
class Event(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  slug = models.SlugField(unique=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

class Location(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  slug = models.SlugField(unique=True)
