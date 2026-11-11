from django.db import models
from core.models import BaseModel

class ProductImages(BaseModel):
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.CASCADE,
        related_name='images'
    )

    product_image = models.ImageField(
        upload_to='media/product/'
        blank=True,
    )