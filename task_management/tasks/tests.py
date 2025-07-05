from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from users.models import User
from tasks.models import Task
from rest_framework_simplejwt.tokens import RefreshToken

class TaskAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            email='test@example.com'  # Required field
        )
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.task_data = {
            'title': 'Sample Task',
            'description': 'This is a sample task.',
        }

    def test_create_task(self):
        response = self.client.post('/api/tasks/', self.task_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.task_data['title'])

    def test_get_tasks(self):
        Task.objects.create(user=self.user, **self.task_data)
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_task(self):
        task = Task.objects.create(user=self.user, **self.task_data)
        updated_data = {
            'title': 'Updated Task',
            'description': 'Updated description.',
        }
        response = self.client.put(f'/api/tasks/{task.id}/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')

    def test_delete_task(self):
        task = Task.objects.create(user=self.user, **self.task_data)
        response = self.client.delete(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
