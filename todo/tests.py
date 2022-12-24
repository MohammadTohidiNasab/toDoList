from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.
class CreateApiTest(APITestCase):
    def test_create(self):
        data = {"id": 1, "Title": "new task", "Description": "testing this",
                "Date": "2022-10-23", "Completed": 'false'}
        response = self.client.post("/api/create", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

