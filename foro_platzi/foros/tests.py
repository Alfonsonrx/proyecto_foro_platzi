import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse
from django.contrib.auth import get_user

from .models import PostModel, CommentModel 
from forum_profile.models import CustomUser 

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
    
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@example.com',nickname='testuser',password='Secret1999')
        
    def test_login_auth(self):
        self.assertFalse(get_user(self.client).is_authenticated)
        self.client.login(email='test@example.com',password='Secret1999')
        self.assertTrue(get_user(self.client).is_authenticated)
        
    def test_no_forums(self):
        self.client.login(email='test@example.com',password='Secret1999')
        response = self.client.get(reverse('foros:Index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No posts are available')
        self.assertQuerysetEqual(response.context['latest_posts'], [])
        
    def test_no_comments_on_forum(self):
        forum = PostModel.objects.create(title='Titulo random', thematic='Tematica', post_text='Post random de testeo', user=self.user)
        f_response = self.client.get(reverse('foros:Foro_detalle', kwargs={'pk':forum.id}))
        
        self.assertEqual(f_response.status_code, 200)
        self.assertContains(f_response, 'There  are no comments yet!')
    
    # def test