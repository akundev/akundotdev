from django.test import TestCase
from django.urls import reverse

from .models import CustomUser

# Create your tests here.
normal_user = {
    "username": "normal",
    "email": "normal@user.com",
    "password": "foo",
    "photo": "https://photo.com/photo.png",
    "github_link": "https://github.com/almazkun",
    "linkedin_link": "https://www.linkedin.com/in/almaz-kunpeissov-7775b541/",
    "cv_link": "/staticfiles/files/A_Kunpeissov_Software_Engineer_Python_CV_ENG_2020_web.docx",
    "public_email": "hello@akun.dev",
}

super_user = {
    "username": "super",
    "email": "super@user.com",
    "password": "foo",
    "photo": "https://photo.com/photo.png",
    "github_link": "https://github.com/almazkun",
    "linkedin_link": "https://www.linkedin.com/in/almaz-kunpeissov-7775b541/",
    "cv_link": "/staticfiles/files/A_Kunpeissov_Software_Engineer_Python_CV_ENG_2020_web.docx",
    "public_email": "hello@akun.dev",
}


class TestAboutTemplateView(TestCase):
    def setUp(self):
        test_obj = normal_user
        CustomUser.objects.create_user(main_user=True, **test_obj)
        author = CustomUser.objects.get(username=test_obj["username"])
        self.main_author = CustomUser.objects.get(username=test_obj["username"])
        self.response = self.client.get(reverse("about"))

    def test_about(self):
        self.assertTemplateUsed(self.response, "users/about.html")
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.context["main_author"], self.main_author)


class UsersManagersTests(TestCase):
    def test_create_user(self):
        test_object = normal_user
        CustomUser.objects.create_user(**test_object)
        obj = CustomUser.objects.get(username=test_object["username"])

        self.assertEqual(obj.username, test_object["username"])
        self.assertEqual(obj.email, test_object["email"])
        self.assertEqual(obj.photo, test_object["photo"])
        self.assertEqual(obj.github_link, test_object["github_link"])
        self.assertEqual(obj.linkedin_link, test_object["linkedin_link"])
        self.assertEqual(obj.cv_link, test_object["cv_link"])
        self.assertEqual(obj.public_email, test_object["public_email"])
        self.assertFalse(obj.main_user)
        self.assertTrue(obj.is_active)
        self.assertFalse(obj.is_staff)
        self.assertFalse(obj.is_superuser)

    def test_create_superuser(self):
        test_object = super_user
        CustomUser.objects.create_superuser(**test_object)
        obj = CustomUser.objects.get(username=test_object["username"])

        self.assertEqual(obj.username, test_object["username"])
        self.assertEqual(obj.email, test_object["email"])
        self.assertEqual(obj.photo, test_object["photo"])
        self.assertEqual(obj.github_link, test_object["github_link"])
        self.assertEqual(obj.linkedin_link, test_object["linkedin_link"])
        self.assertEqual(obj.cv_link, test_object["cv_link"])
        self.assertEqual(obj.public_email, test_object["public_email"])
        self.assertFalse(obj.main_user)
        self.assertTrue(obj.is_active)
        self.assertTrue(obj.is_staff)
        self.assertTrue(obj.is_superuser)

    def test_only_one_main_user(self):
        CustomUser.objects.create_superuser(main_user=True, **super_user)
        CustomUser.objects.create_user(main_user=True, **normal_user)
        obj = CustomUser.objects.get(username=super_user["username"])
        test_object = CustomUser.objects.get(username=normal_user["username"])

        self.assertTrue(obj.main_user)
        self.assertTrue(test_object.main_user)
