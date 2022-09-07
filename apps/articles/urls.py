from django.urls import path

from .views import ArticleDetailView, ArticleListView, HomepageListView, TagDetailView

urlpatterns = [
    path("", HomepageListView.as_view(), name="home"),
    path("articles/", ArticleListView.as_view(), name="articles"),
    path("articles/<slug:slug>", ArticleDetailView.as_view(), name="article_detail"),
    path("t/<slug:slug>", TagDetailView.as_view(), name="tag_detail"),
]
