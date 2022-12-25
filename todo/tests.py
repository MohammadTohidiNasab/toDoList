from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Todo


# Create your tests here.
class TodoApiTest(APITestCase):
    def test_create(self):
        data = {"id": 1, "Title": "new task", "Description": "testing this",
                "Date": "2022-10-23", "Completed": 'false'}
        response = self.client.post("/api/create", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.get().Title, 'new task')

