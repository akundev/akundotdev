from django.test import TestCase
from django.urls import reverse

from apps.articles.models import Tag
from apps.users.models import CustomUser

from .models import Tool

# Create your tests here.
test_tool = {
    "name": "tool_name",
    "slug": "tool_slug",
    "description": "tool_description",
    "img_link": "https://tool_img_link.com/tool.png",
    "link": "https://tool_link.com",
}

test_tag = {
    "tag_name": "test_tag",
    "img_link": "https://test_tag.org/test.png",
    "description": "long test description",
    "slug": "test_tag",
    "source_link": "https://test_tag.org/",
}

normal_user = {"username": "normal", "email": "normal@user.com", "password": "foo"}


class TestToolsModels(TestCase):
    def setUp(self):
        self.test_obj = test_tool
        self.test_tag = test_tag
        tool = Tool.objects.create(**self.test_obj)
        tool.tags.add(Tag.objects.create(**self.test_tag))
        tool.save()

    def test_tool_created(self):
        obj = Tool.objects.get(name=self.test_obj["name"])

        self.assertEqual(obj.name, self.test_obj["name"])
        self.assertEqual(obj.slug, self.test_obj["slug"])
        self.assertEqual(obj.description, self.test_obj["description"])
        self.assertEqual(obj.img_link, self.test_obj["img_link"])
        self.assertEqual(obj.link, self.test_obj["link"])
        self.assertEqual(obj.tags.all()[0].tag_name, self.test_tag["tag_name"])


class TestToolsListViews(TestCase):
    def setUp(self):
        self.test_obj = test_tool
        self.test_tag = test_tag
        self.test_user = normal_user
        CustomUser.objects.create_user(**self.test_user)
        tool = Tool.objects.create(**self.test_obj)
        tool.tags.add(Tag.objects.create(**self.test_tag))
        tool.save()

    def test_tools_list_view(self):
        obj = Tool.objects.all()
        response = self.client.get(reverse("tools_list"))

        self.assertQuerysetEqual(response.context["tools"], obj, transform=lambda x: x)
        self.assertTemplateUsed(response, "tools/tools_list.html")
        self.assertEqual(response.status_code, 200)

    def test_main_author(self):
        main_author = CustomUser.objects.get(username=self.test_user["username"])
        main_author.main_user = True
        main_author.save()
        response = self.client.get(reverse("tools_list"))

        self.assertEqual(response.context["main_author"], main_author)


class TestToolsDetailViews(TestCase):
    def setUp(self):
        self.test_obj = test_tool
        self.test_tag = test_tag
        self.test_user = normal_user
        CustomUser.objects.create_user(**self.test_user)
        tool = Tool.objects.create(**self.test_obj)
        tool.tags.add(Tag.objects.create(**self.test_tag))
        tool.save()

    def test_tools_detail_view(self):
        obj = Tool.objects.get(name=self.test_obj["name"])
        response = self.client.get(
            reverse("tool_detail", kwargs={"slug": self.test_obj["slug"]})
        )

        self.assertEqual(response.context["tool"], obj)
        self.assertTemplateUsed(response, "tools/tool_detail.html")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["tool"].name, self.test_obj["name"])
        self.assertEqual(response.context["tool"].slug, self.test_obj["slug"])
        self.assertEqual(
            response.context["tool"].description, self.test_obj["description"]
        )
        self.assertEqual(response.context["tool"].img_link, self.test_obj["img_link"])
        self.assertEqual(response.context["tool"].link, self.test_obj["link"])
        self.assertEqual(
            response.context["tool"].tags.all()[0].tag_name, self.test_tag["tag_name"]
        )

    def test_main_author(self):
        main_author = CustomUser.objects.get(username=self.test_user["username"])
        main_author.main_user = True
        main_author.save()
        response = self.client.get(reverse("tools_list"))

        self.assertEqual(response.context["main_author"], main_author)
