from core.models import BaseModel
from django.db import models
from django.conf import settings

class Comments(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    product = models.ForeignKey(
        'costumer.Customer',
        on_delete=models.CASCADE,
        related_name='comments'
    )

    message = models.TextField(
        max_length=200
    )