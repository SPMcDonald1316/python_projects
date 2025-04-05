from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            email="test@user.com",
            password="testpass123",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(
            username="testsuper",
            email="super@user.com",
            password="superPass",
        )
        self.assertEqual(superuser.username, "testsuper")
        self.assertEqual(superuser.email, "super@user.com")
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)


class SignUpPageTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Log In")
