from django.db import models
from core.models import BaseModel, SluggedMixinModel
from django.utils.text import slugify
class Category(SluggedMixinModel, BaseModel):
    title = models.CharField(
        max_length=50,
        unique=True,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        max_length=255
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)