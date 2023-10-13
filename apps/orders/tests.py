from django.test import TestCase
from django.urls import reverse

from apps.shop.models import Product
from apps.users.models import CustomUser

from .models import Order

test_order = {"name": "Django Django", "email": "django@django.some", "paid": True}

test_product = {
    "name": "Test Product",
    "abbr": "TEPR",
    "slug": "tepr",
    "description": "Test Product description",
    "price": 2000,
}

normal_user = {"username": "normal", "email": "normal@user.com", "password": "foo"}


# Create your tests here.
class TestOrderModelCreation(TestCase):
    """Test Product Model Creation"""

    def setUp(self):
        self.test_order = test_order
        self.test_product = test_product
        Order.objects.create(
            **self.test_order, product=Product.objects.create(**self.test_product)
        )

    def test_order_model_created(self):
        obj = Order.objects.get(name=self.test_order["name"])

        self.assertEqual(obj.name, self.test_order["name"])
        self.assertEqual(obj.email, self.test_order["email"])
        self.assertEqual(obj.paid, self.test_order["paid"])
        self.assertEqual(obj.product.name, self.test_product["name"])


class TestOrderCreateView(TestCase):
    """Test Order Create View"""

    def setUp(self):
        self.test_order = test_order
        self.test_product = test_product
        self.test_user = normal_user
        CustomUser.objects.create_user(**self.test_user)
        Order.objects.create(
            **self.test_order, product=Product.objects.create(**self.test_product)
        )

    def test_order_create_view(self):
        response = self.client.get(reverse("order_create"))

        self.assertTemplateUsed(response, "orders/order_form.html")
        self.assertEqual(response.status_code, 200)


class TestSuccessView(TestCase):
    """Test Success View"""

    def setUp(self):
        self.test_user = normal_user
        CustomUser.objects.create_user(**self.test_user)

    def test_order_success_view(self):
        response = self.client.get(reverse("success_created"))

        self.assertTemplateUsed(response, "orders/success_created.html")
        self.assertEqual(response.status_code, 200)
