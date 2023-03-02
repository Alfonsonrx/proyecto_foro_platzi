import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse

from .models import PostModel, CommentModel 

class PostModelTest(TestCase):
    def setUp(self):
        self.post = PostModel(title='Titulo random', thematic='Tematica', post_text='Post random de testeo')
    
    def test_recently_published_future(self):
        time = timezone.now() + datetime.timedelta(days=15)
        self.post.pub_date = time
        self.assertFalse(self.post.was_published_recently())
    
    def test_recently_published_past(self):
        time = timezone.now() + datetime.timedelta(days=-15)
        self.post.pub_date = time
        self.assertFalse(self.post.was_published_recently())
    
    def test_recently_published_present(self):
        time = timezone.now()
        self.post.pub_date = time
        self.assertTrue(self.post.was_published_recently())
    
class ForosViewsTest(TestCase):
    
    def test_no_forums(self):
        response = self.client.get(reverse('foros:Index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No posts are available')
        self.assertQuerysetEqual(response.context['latest_posts'], [])
        
    