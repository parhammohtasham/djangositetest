from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

class PostTestList(TestCase):
    def setUp(self):
        Post.objects.create(text='ttt')

    def test_setUp(self):
        post = Post.objects.get(id=1)
        excepted_object_name=f'{post}'
        self.assertEqual(excepted_object_name,'ttt')

    def test_post_string_model(self):
        post =  Post(text='hello')
        self.assertEqual(str(post),post.text)

class PostTestView(TestCase):
    def test_posts_page_urls(self):
        response=self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'posts/list.html')