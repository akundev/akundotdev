from django.db import models
from django.urls import reverse

from apps.articles.models import Tag


# Create your models here.
class Tool(models.Model):
    name = models.CharField(verbose_name="Tool", max_length=150)
    slug = models.SlugField(verbose_name="Slug", unique=True)
    description = models.CharField(verbose_name="Description", max_length=280)
    img_link = models.CharField(verbose_name="Image url", max_length=255)
    link = models.CharField(verbose_name="Url of the tool", max_length=255)
    tags = models.ManyToManyField(Tag, verbose_name="Tags")

    class Meta:
        verbose_name = "Tool"
        verbose_name_plural = "Tools"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tool_detail", args=[self.slug])
