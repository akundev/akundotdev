from django.views.generic import DetailView, ListView

from apps.shop.models import Product
from apps.tools.models import Tool

from .models import Article, Tag


class HomepageListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "articles/home.html"
    queryset = Article.objects.all().is_published()[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tools"] = Tool.objects.all()[:5]
        context["products"] = Product.objects.all()[:5]
        return context


class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "articles/articles.html"
    queryset = Article.objects.all().is_published()


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "articles/article_detail.html"

    def get_object(self):
        obj = super(DetailView, self).get_object()
        obj.update_views()
        obj.content = obj.content_to_markdown()
        return obj


class TagDetailView(DetailView):
    model = Tag
    context_object_name = "tag"
    template_name = "articles/tag_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = self.object.article_set.all()
        context["tools"] = self.object.tool_set.all()
        context["products"] = self.object.product_set.all()
        return context
