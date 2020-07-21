from django.test import TestCase
from django.urls import reverse

import markdown

from .models import Tag, Article
from apps.users.models import CustomUser
from apps.tools.models import Tool


test_tag = {
    "tag_name": "test_tag",
    "img_link": "https://test_tag.org/test.png",
    "description": "long test description",
    "slug": "test_tag",
    "source_link": "https://test_tag.org/",
}

test_article = {
    "title": "test_article",
    "slug": "test_article",
    "description": "long test description",
    "content": "# long test context",
    "img_link": "https://test_tag.org/test.png",
    "views": 100,
    "is_published": True,
}

test_article_not_pub = {
    "title": "test_article_not_pub",
    "slug": "test_article_not_pub",
    "description": "long test description_not_pub",
    "content": "long test context_not_pub",
    "img_link": "https://test_tag.org/test.png",
    "views": 500,
    "is_published": False,
}


normal_user = {"username": "normal", "email": "normal@user.com", "password": "foo"}

test_tool = {
    "name": "tool_name",
    "slug": "tool_slug",
    "description": "tool_description",
    "img_link": "https://tool_img_link.com/tool.png",
    "link": "https://tool_link.com",
}


# Create your tests here.
class TestTagModel(TestCase):
    def test_tag_model(self):
        Tag.objects.create(**test_tag)
        obj = Tag.objects.get(tag_name=test_tag["tag_name"])

        self.assertEqual(obj.tag_name, test_tag["tag_name"])
        self.assertEqual(obj.img_link, test_tag["img_link"])
        self.assertEqual(obj.description, test_tag["description"])
        self.assertEqual(obj.slug, test_tag["slug"])
        self.assertEqual(obj.source_link, test_tag["source_link"])


class TestArticleModel(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(**normal_user)
        author = CustomUser.objects.get(username=normal_user["username"])
        test_article["author"] = author
        test_article_not_pub["author"] = author
        Article.objects.create(**test_article)
        Article.objects.create(**test_article_not_pub)

    def test_article_model(self):
        test_obj = test_article
        obj = Article.objects.get(title=test_obj["title"])

        self.assertEqual(obj.title, test_obj["title"])
        self.assertEqual(obj.slug, test_obj["slug"])
        self.assertEqual(obj.author, test_obj["author"])
        self.assertEqual(obj.description, test_obj["description"])
        self.assertEqual(obj.content, test_obj["content"])
        self.assertEqual(obj.img_link, test_obj["img_link"])
        self.assertEqual(obj.views, test_obj["views"])
        self.assertEqual(obj.is_published, test_obj["is_published"])

    def test_article_not_pub(self):
        test_obj = test_article_not_pub
        obj = Article.objects.get(title=test_obj["title"])

        self.assertEqual(obj.title, test_obj["title"])
        self.assertEqual(obj.slug, test_obj["slug"])
        self.assertEqual(obj.author, test_obj["author"])
        self.assertEqual(obj.description, test_obj["description"])
        self.assertEqual(obj.content, test_obj["content"])
        self.assertEqual(obj.img_link, test_obj["img_link"])
        self.assertEqual(obj.views, test_obj["views"])
        self.assertEqual(obj.is_published, test_obj["is_published"])

    def test_article_manager(self):
        obj = Article.objects.all()
        obj_is_pub = Article.objects.all().is_published()

        self.assertEqual(obj.count(), 2)
        self.assertEqual(obj_is_pub.count(), 1)

    def test_article_markdown(self):
        test_obj = test_article
        obj = Article.objects.get(pk=1)
        md = markdown.Markdown(extensions=["markdown.extensions.extra"])

        self.assertEqual(obj.content_to_markdown(), md.convert(test_obj["content"]))

    def test_views(self):
        test_obj = test_article
        obj = Article.objects.get(title=test_obj["title"])
        obj.update_views()

        self.assertEqual(obj.views, test_obj["views"] + 1)


class TestHomepageListView(TestCase):
    def setUp(self):
        self.test_tool = test_tool
        CustomUser.objects.create_user(**normal_user)
        author = CustomUser.objects.get(username=normal_user["username"])
        test_article["author"] = author
        test_article_not_pub["author"] = author
        Article.objects.create(**test_article)
        Article.objects.create(**test_article_not_pub)
        Tool.objects.create(**self.test_tool)


    def test_home(self):
        obj_is_pub = Article.objects.all().is_published()
        test_tool = Tool.objects.get(name=self.test_tool["name"])
        response = self.client.get(reverse("home"))

        self.assertQuerysetEqual(
            response.context["articles"], obj_is_pub, transform=lambda x: x
        )
        self.assertEqual(response.context["tools"][0], test_tool)
        self.assertTemplateUsed(response, "articles/home.html")
        self.assertEqual(response.status_code, 200)
        
        

    def test_main_author(self):
        main_author = CustomUser.objects.get(username=normal_user["username"])
        main_author.main_user = True
        main_author.save()
        response = self.client.get(reverse("home"))

        self.assertEqual(response.context["main_author"], main_author)


class TestArticleListView(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(**normal_user)
        author = CustomUser.objects.get(username=normal_user["username"])
        test_article["author"] = author
        test_article_not_pub["author"] = author
        Article.objects.create(**test_article)
        Article.objects.create(**test_article_not_pub)

    def test_articles(self):
        obj_is_pub = Article.objects.all().is_published()
        response = self.client.get(reverse("articles"))

        self.assertQuerysetEqual(
            response.context["articles"], obj_is_pub, transform=lambda x: x
        )
        self.assertTemplateUsed(response, "articles/articles.html")
        self.assertEqual(response.status_code, 200)

    def test_main_author(self):
        main_author = CustomUser.objects.get(username=normal_user["username"])
        main_author.main_user = True
        main_author.save()
        response = self.client.get(reverse("articles"))

        self.assertEqual(response.context["main_author"], main_author)


class TestArticleDetailView(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(**normal_user)
        test_article["author"] = CustomUser.objects.get(
            username=normal_user["username"]
        )
        Article.objects.create(**test_article)

    def test_article_detail(self):
        obj = Article.objects.get(title=test_article["title"])
        response = self.client.get(
            reverse("article_detail", kwargs={"slug": test_article["slug"]})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "articles/article_detail.html")

    def test_main_author(self):
        main_author = CustomUser.objects.get(username=normal_user["username"])
        main_author.main_user = True
        main_author.save()
        response = self.client.get(
            reverse("article_detail", kwargs={"slug": test_article["slug"]})
        )

        self.assertEqual(response.context["main_author"], main_author)


class TestTagDetailView(TestCase):
    def setUp(self):
        self.test_tag = test_tag
        self.test_user = normal_user
        self.test_article = test_article

        CustomUser.objects.create_user(**normal_user)
        self.test_article["author"] = CustomUser.objects.get(
            username=self.test_user["username"]
        )
        article = Article.objects.create(**self.test_article)
        article.tags.add(Tag.objects.create(**self.test_tag))
        article.save()

    def test_article_detail(self):
        article = Article.objects.filter(tags__tag_name=self.test_tag["tag_name"])
        response = self.client.get(
            reverse("tag_detail", kwargs={"slug": self.test_tag["slug"]})
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["tag"].tag_name, self.test_tag["tag_name"])
        self.assertEqual(response.context["tag"].img_link, self.test_tag["img_link"])
        self.assertEqual(
            response.context["tag"].description, self.test_tag["description"]
        )
        self.assertEqual(response.context["tag"].slug, self.test_tag["slug"])
        self.assertEqual(
            response.context["tag"].source_link, self.test_tag["source_link"]
        )
        self.assertEqual(str(response.context["articles"]), str(article))
        self.assertTemplateUsed(response, "articles/tag_detail.html")

    def test_main_author(self):
        main_author = CustomUser.objects.get(username=self.test_user["username"])
        main_author.main_user = True
        main_author.save()

        response = self.client.get(
            reverse("tag_detail", kwargs={"slug": self.test_tag["slug"]})
        )

        self.assertEqual(response.context["main_author"], main_author)
