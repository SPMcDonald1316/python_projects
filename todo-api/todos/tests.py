from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="a todo",
            body="doing something",
        )

    def test_todo_model(self):
        self.assertEqual(self.todo.title, "a todo")
        self.assertEqual(self.todo.body, "doing something")
        self.assertEqual(str(self.todo), "a todo")

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "a todo")
