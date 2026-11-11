from core.models import *
from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator

discount_validator = [MinValueValidator(0), MaxValueValidator(100)]

gender_choices = (
    ('Male', 'male'),
    ('Female', 'female')
)

matterials = (
    ('Plastic', 'plastic'),
    ('Leather', 'leather'),
    ('Steel', 'steel'),
)

class Product(BaseModel,SluggedMixinModel):

    brand = models.ForeignKey(
        'product.Brand',
        on_delete=models.PROTECT,
        related_name='products'
    )

    category = models.ForeignKey(
        'product.Category',
        on_delete=models.PROTECT,
        related_name='products'
    )


    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False
    )

    discount_percentage =  models.SmallIntegerField(
        default=0,
        validators=discount_validator
        )

    price = models.DecimalField(
        max_digits=15,
        decimal_places=0,
        default=Decimal(0),
        validators=[MinValueValidator(0)]
    )

    is_avalible = models.BooleanField(
        default=True
    )

    is_luxury = models.BooleanField(
        default=False
    )

    is_special = models.BooleanField(
        default=False
    )

    is_stash = models.BooleanField(
        default=False
    )

    gender = models.CharField(
        max_length=10,
        choices=gender_choices
    )

    origin = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    Strap_matterial = models.CharField(
        max_length=10,
        choices=matterials
    )

    description = models.TextField(
        max_length=255,
        blank=True,
    )

    main_image = models.ImageField(
        blank=True,
        )

    fetures = models.JSONField(
        default=dict,
        blank=True,
    )

    views = models.IntegerField(
        default=0,
    )

    # def link_clicked(self, *args, **kwargs):
    #     self.views += 1       
    #     return super().save(*args, **kwargs)