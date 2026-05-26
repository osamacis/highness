from django.test import TestCase
from django.urls import reverse
from .models import ContactInquiry

class PagesViewsTestCase(TestCase):
    def test_home_page_view(self):
        url = reverse('pages:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_about_page_view(self):
        url = reverse('pages:about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about.html')

    def test_contact_page_view(self):
        url = reverse('pages:contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/contact.html')

    def test_contact_form_submission(self):
        url = reverse('pages:contact')
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'phone': '1234567890',
            'subject': 'Test Subject',
            'message': 'This is a test message from unit tests.'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302) # Redirect on success
        self.assertTrue(ContactInquiry.objects.filter(email='test@example.com').exists())
