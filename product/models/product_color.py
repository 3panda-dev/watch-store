from django.db import models

class ProductColor(models.Model):
    product = models.ForeignKey(
        "product.Product",
        on_delete=models.CASCADE,
        related_name='colors'
    )

    color = models.CharField(
        max_length=20,
    )

    hex_code = models.CharField(
        max_length=7,
        default='#ffffff'
    )