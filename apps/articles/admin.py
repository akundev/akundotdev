from django.contrib import admin

from .models import Article, Tag

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ["tag_name"]
    prepopulated_fields = {"slug": ("tag_name",)}


admin.site.register(Tag, TagAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "views", "is_published", "created_on"]

    list_filter = ["views", "is_published", "created_on"]
    list_editable = ["is_published"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)
