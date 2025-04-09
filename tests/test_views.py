from django.test import TestCase
from restaurant.models import MenuItem
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        MenuItem.objects.create(title="Pizza", price=120.00, inventory=15)
        MenuItem.objects.create(title="Burger", price=80.00, inventory=25)
        MenuItem.objects.create(title="Fries", price=50.00, inventory=30)

    def test_getall(self):
        url = '/restaurant/menu/'  # Adjusted URL
        response = self.client.get(url)
    
        # Debugging: Print response details if needed
        print("Response status:", response.status_code)
        print("Response content:", response.content)
    
        # Fetch and serialize data
        menu_items = MenuItem.objects.all()
        serialized_data = [
            {"title": item.title, "price": str(item.price), "inventory": item.inventory}
            for item in menu_items
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serialized_data)

