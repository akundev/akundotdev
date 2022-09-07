from django.test import TestCase
from django.urls import reverse

from apps.articles.models import Tag
from apps.users.models import CustomUser

from .models import Product

test_product = {
    "name": "Test Product",
    "abbr": "TEPR",
    "slug": "tepr",
    "description": "Test Product description",
    "price": 2000,
}

test_tag = {
    "tag_name": "test_tag",
    "img_link": "https://test_tag.org/test.png",
    "description": "long test description",
    "slug": "test_tag",
    "source_link": "https://test_tag.org/",
}

normal_user = {"username": "normal", "email": "normal@user.com", "password": "foo"}


# Create your tests here.
class TestProductModelCreation(TestCase):
    """Test Product Model Creation"""

    def setUp(self):
        self.test_pro = test_product
        self.test_tag = test_tag
        Product.objects.create(**self.test_pro)
        pro = Product.objects.get(name=self.test_pro["name"])
        pro.tags.add(Tag.objects.create(**self.test_tag))
        pro.save()

    def test_pro_created(self):
        pro = Product.objects.get(name=self.test_pro["name"])

        self.assertEqual(pro.name, self.test_pro["name"])
        self.assertEqual(pro.abbr, self.test_pro["abbr"])
        self.assertEqual(pro.slug, self.test_pro["slug"])
        self.assertEqual(pro.description, self.test_pro["description"])
        self.assertEqual(pro.price, self.test_pro["price"])
        self.assertEqual(pro.tags.all()[0].tag_name, self.test_tag["tag_name"])


class TestProductListView(TestCase):
    """Test Product List View"""

    def setUp(self):
        self.test_pro = test_product
        self.test_tag = test_tag
        self.test_user = normal_user
        CustomUser.objects.create_user(**self.test_user)
        Product.objects.create(**self.test_pro)
        pro = Product.objects.get(name=self.test_pro["name"])
        pro.tags.add(Tag.objects.create(**self.test_tag))
        pro.save()

    def test_product_list_view(self):
        obj = Product.objects.all()
        response = self.client.get(reverse("products_list"))

        self.assertQuerysetEqual(
            response.context["products"], obj, transform=lambda x: x
        )
        self.assertTemplateUsed(response, "shop/products_list.html")
        self.assertEqual(response.status_code, 200)

    def test_main_author(self):
        main_author = CustomUser.objects.get(username=self.test_user["username"])
        main_author.main_user = True
        main_author.save()
        response = self.client.get(reverse("products_list"))

        self.assertEqual(response.context["main_author"], main_author)


class TestProductsDetailViews(TestCase):
    def setUp(self):
        self.test_pro = test_product
        self.test_tag = test_tag
        self.test_user = normal_user
        CustomUser.objects.create_user(**self.test_user)
        Product.objects.create(**self.test_pro)
        pro = Product.objects.get(name=self.test_pro["name"])
        pro.tags.add(Tag.objects.create(**self.test_tag))
        pro.save()

    def test_product_detail_view(self):
        obj = Product.objects.get(name=self.test_pro["name"])
        response = self.client.get(
            reverse("product_detail", kwargs={"slug": self.test_pro["slug"]})
        )

        self.assertEqual(response.context["product"], obj)
        self.assertTemplateUsed(response, "shop/product_detail.html")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["product"].name, self.test_pro["name"])
        self.assertEqual(response.context["product"].abbr, self.test_pro["abbr"])
        self.assertEqual(response.context["product"].slug, self.test_pro["slug"])
        self.assertEqual(
            response.context["product"].description, self.test_pro["description"]
        )
        self.assertEqual(response.context["product"].price, self.test_pro["price"])
        self.assertEqual(
            response.context["product"].tags.all()[0].tag_name,
            self.test_tag["tag_name"],
        )

    def test_main_author(self):
        main_author = CustomUser.objects.get(username=self.test_user["username"])
        main_author.main_user = True
        main_author.save()
        response = self.client.get(reverse("products_list"))

        self.assertEqual(response.context["main_author"], main_author)
