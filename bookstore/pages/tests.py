from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import AboutPageView, HomePageView


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "home.html")
        self.assertContains(self.response, "home page")
        self.assertNotContains(self.response, "Hi there!")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_aboutpage(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "about.html")
        self.assertContains(self.response, "About Page")
        self.assertNotContains(self.response, "Home")

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
