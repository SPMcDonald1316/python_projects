from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Book Title",
            subtitle="Book Subtitle",
            author="Book Author",
            isbn="Book ISBN",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "Book Title")
        self.assertEqual(self.book.subtitle, "Book Subtitle")
        self.assertEqual(self.book.author, "Book Author")
        self.assertEqual(self.book.isbn, "Book ISBN")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "books/book_list.html")
        self.assertContains(response, "Book Title")
