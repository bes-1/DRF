from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, APITestCase
from rest_framework import status
from .views import UserModelViewSet
from usersapp.models import User
from notesapp.models import ToDo
from mixer.backend.django import mixer


class TestUserApi(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_get_list_1(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users')
        view = UserModelViewSet.as_view({'get': 'list'})
        User.objects.create(first_name='Anton', last_name='Bogoslavski')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_list_2(self):
        client = APIClient()
        response = client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


class TestUserClientApi(APITestCase):

    def setUp(self) -> None:
        self.user = mixer.blend(User)
        self.todo = mixer.blend(ToDo, project__link_to_repository='qqq.ru')
        self.admin = User.objects.create_superuser('TestApi', email='TestApi@gb.com', password='geekbrains')

    # def test_get_list_3(self):      # тест при отключении permission
    #     response = self.client.get('/api/users/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 0)

    def test_get_list_3(self):  # тест при отключении permission
        self.client.login(username='TestApi', password='geekbrains')
        response = self.client.get('/api/users/')
        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_4(self):
        User.objects.create(first_name='Anton', last_name='Bogoslavski')
        # self.client.login(username='TestApi', password='geekbrains')
        self.client.force_login(self.admin)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_5(self):
        self.client.force_login(self.admin)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
