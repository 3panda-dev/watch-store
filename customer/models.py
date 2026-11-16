from django.db import models
from django.utils.text import slugify
from core.models import *
from django.dispatch import receiver, post_save
from django.contrib.auth.models import User

class Customer(BaseModel, SluggedMixinModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customer'

    )

    phone_number = models.CharField(max_length=11, unique=True)

#note add signals so after a user is created a customer profile also gets
# created with the same phone number


@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance, phone_number=instance.phone_number)