from django.test import TestCase

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
