from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title="Post Title",
            body="Post Body",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "Post Title")
        self.assertEqual(self.post.body, "Post Body")
        self.assertEqual(str(self.post), "Post Title")
