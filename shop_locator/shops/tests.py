from django.test import TestCase
from django.urls import reverse
from .models import Shop

# Create your tests here.

class ShopListViewTests(TestCase):
    def test_shop_list_view_with_results(self):
        Shop.objects.create(name='Test Shop', latitude=51.5074, longitude=-0.1278)

        response = self.client.get(reverse('shop_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Shop')

    def test_shop_list_view_no_results(self):
        response = self.client.get(reverse('shop_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No shops found within the specified distance.')
