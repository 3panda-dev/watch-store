from django.db import models
from django.utils.text import slugify

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SluggedMixinModel(models.Model):
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=False,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super.save(*args,**kwargs)

    class Meta:
        abstract = True