from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        # Create test Menu items
        self.item1 = Menu.objects.create(title="Burger", price=150, inventory=10)
        self.item2 = Menu.objects.create(title="Pizza", price=250, inventory=5)
        self.item3 = Menu.objects.create(title="Pasta", price=180, inventory=8)

    def test_getall(self):
        # Call the GET endpoint that lists all menu items
        response = self.client.get(reverse('menu-list'))  # Adjust the name if needed

        # Get all Menu objects and serialize them
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Assert that response data matches serialized data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
