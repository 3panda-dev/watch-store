from core.models import BaseModel
from django.db import models

class Comments(BaseModel):
    user = models.ForeignKey(
        'auth.User',
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