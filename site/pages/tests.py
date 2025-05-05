from django.test import TestCase

# Create your tests here.

class PageViewTest(TestCase):
    def test_home_page_view(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pages/home.html')

    def test_about_page_view(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pages/about.html')