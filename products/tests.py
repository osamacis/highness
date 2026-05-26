from django.test import TestCase
from django.urls import reverse
from .models import Category, Product

class ProductViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Cereals",
            slug="test-cereals"
        )
        self.product = Product.objects.create(
            name="Test Cereal Product",
            slug="test-cereal-product",
            category=self.category,
            short_description="A test product",
            description="Detailed test description",
            ingredients="None",
            weight="100g",
            mrp=100.00,
            selling_price=90.00
        )

    def test_category_list_view(self):
        url = reverse('products:category_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/category_list.html')

    def test_product_list_view(self):
        url = reverse('products:product_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')

    def test_product_list_by_category_view(self):
        url = reverse('products:product_list_by_category', kwargs={'category_slug': self.category.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')

    def test_product_detail_view(self):
        url = reverse('products:product_detail', kwargs={'slug': self.product.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertContains(response, self.product.name)
