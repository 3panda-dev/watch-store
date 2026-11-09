from core.models import *
from django.db import models

class Brand(SluggedMixinModel, BaseModel):
    name = models.CharField(unique=True,
                            blank=False,
                            max_length=100,
                            )
    
    meta_title = models.CharField(unique=False,
                                  blank=True,
                                  null=True,
                                  max_length=50
                                  )

    meta_description = models.TextField(max_length=300,
                                        unique=False,
                                        blank=True
                                        )

    class Meta:
        ordering = ['name']