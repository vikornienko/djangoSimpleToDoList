

from django.test import TestCase
from django.test import Client

from .models import Todo


class TodoModelTests(TestCase):
    def setUp(self):
        Todo.objects.create(name="My todo first record.", due_date="2022-10-31")
        Todo.objects.create(name="My second record.", due_date="2022-11-01")
    def test_todo_model(self):
        first_record = Todo.objects.get(name="My todo first record.")
        second_record = Todo.objects.get(name="My second record.")
        self.assertEqual(first_record.name, 'My todo first record.')
        self.assertEqual(second_record.name, "My second record.")

class TodoViewTests(TestCase):
    def test_todo_view(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)



