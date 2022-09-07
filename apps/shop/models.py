from django.db import models
from django.urls import reverse

from apps.articles.models import Tag


# Create your models here.
class Product(models.Model):
    name = models.CharField(verbose_name="Product", max_length=150)
    abbr = models.CharField(verbose_name="Abbreviation", max_length=4)
    slug = models.SlugField(verbose_name="Slug", unique=True)
    description = models.CharField(verbose_name="Description", max_length=280)
    price = models.PositiveSmallIntegerField(verbose_name="Price")
    full_description = models.TextField(verbose_name="full_description")
    tags = models.ManyToManyField(Tag, verbose_name="Tags")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.slug])

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Product"
