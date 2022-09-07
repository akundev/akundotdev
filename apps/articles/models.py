import markdown
from django.db import models
from django.urls import reverse

from apps.users.models import CustomUser


class ArticleQuerySet(models.QuerySet):
    def is_published(self):
        return self.filter(is_published=True)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)


class Tag(models.Model):
    tag_name = models.CharField(verbose_name="Tag", max_length=150)
    img_link = models.CharField(verbose_name="Image url", max_length=255)
    description = models.CharField(verbose_name="Description", max_length=280)
    slug = models.SlugField(verbose_name="Slug", unique=True)
    source_link = models.CharField(verbose_name="Sources url", max_length=255)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["tag_name"]

    def __str__(self):
        return self.tag_name

    def get_absolute_url(self):
        return reverse("tag_detail", args=[self.slug])


class Article(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100)
    slug = models.SlugField(verbose_name="Slug", unique=True)
    author = models.ForeignKey(
        CustomUser, verbose_name="Author", on_delete=models.CASCADE
    )
    description = models.CharField(verbose_name="Description", max_length=280)
    content = models.TextField(verbose_name="Content", help_text="Use Markdown syntax")
    img_link = models.CharField(verbose_name="Image url", max_length=255)
    created_on = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name="Updated", auto_now=True)
    views = models.IntegerField(verbose_name="Views", default=0)
    is_published = models.BooleanField("Published", default=False)
    tags = models.ManyToManyField(Tag, verbose_name="Tags")

    objects = ArticleManager()

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-created_on"]

    def __str__(self):
        return self.title[:20]

    def update_views(self):
        self.views += 1
        self.save(update_fields=["views"])

    def content_to_markdown(self):
        md = markdown.Markdown(extensions=["markdown.extensions.extra"])
        return md.convert(self.content)

    def get_absolute_url(self):
        return reverse("article_detail", args=[self.slug])
