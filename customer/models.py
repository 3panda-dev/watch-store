from django.db import models
from django.utils.text import slugify

class Profile(models.Model):
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
