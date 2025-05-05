from django.test import TestCase
from .models import Blog
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

class BlogTest(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='mohammad',
            password='123'
        )
        self.blog = Blog.objects.create(
            title='blog.title',
            body='blog.body',
            author=self.user
            )
        
    def test_setup(self):
        self.assertEqual(f'{self.blog.title}','blog.title')
        self.assertEqual(f'{self.blog.body}','blog.body')
        self.assertEqual(f'{self.blog.author}','mohammad')

    def test_blog_string_model(self):
        blog=Blog(title='hello world')
        self.assertEqual(str(blog),blog.title)

    def test_blog_list_view(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'blog/list.html')

    def test_blog_detail_view(self):
        response=self.client.get('/blog/1/')
        no_response=self.client.get('/blog/10/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertTemplateUsed(response,'blog/detail.html')

    def test_get_absolute_url(self):
        self.assertEqual(self.blog.get_absolute_url(),'/blog/1/')

    def test_create_blog(self):
        response = self.client.post(reverse('blog_new'),{
            'title':'new_title',
            'body':'new_body',
            'author':self.user.id,
        })
        self.assertEqual(response.status_code,302)
        self.assertEqual(Blog.objects.last().title,'new_title')
        self.assertEqual(Blog.objects.last().body,'new_body')

    def test_update_blog(self):
        response=self.client.post(reverse('blog_update',args='1'),{
            'title':'updated_title',
            'body':'updated_body',
        })
        self.assertEqual(response.status_code,302)

    def test_delete_blog(self):
        response=self.client.post(reverse('blog_delete',args='1'))
        self.assertEqual(response.status_code,302)

    