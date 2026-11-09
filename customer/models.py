from django.db import models
from django.utils.text import slugify
from core.models import *

class Cutomer(BaseModel, SluggedMixinModel):
    user = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='customer'

    )

    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=11, unique=True)

#note add signals so after a user is created a customer profile also gets
# created with the same phone number