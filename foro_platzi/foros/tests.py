import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse
from django.contrib.auth import get_user

from .models import PostModel, CommentModel 
from forum_profile.models import CustomUser 

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@example.com',nickname='testuser',password='Secret1999')
        self.forum = PostModel.objects.create(title='Titulo random', thematic='Tematica', post_text='Post random de testeo', user=self.user)
        self.comment = CommentModel(user=self.user,post=self.forum, text_comment='Comentario random de testeo')
    
    def test_recently_published_past(self):
        time = timezone.now() + datetime.timedelta(days=-15)
        self.comment.pub_date = time
        self.assertFalse(self.comment.was_published_recently())
    
    def test_recently_published(self):
        time = timezone.now()
        self.comment.pub_date = time
        self.assertTrue(self.comment.was_published_recently())

class PostModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@example.com',nickname='testuser',password='Secret1999')
        self.forum = PostModel(title='Titulo random', thematic='Tematica', post_text='Post random de testeo', user=self.user)
    
    def test_recently_published_past(self):
        time = timezone.now() + datetime.timedelta(days=-15)
        self.forum.pub_date = time
        self.assertFalse(self.forum.was_published_recently())
    
    def test_recently_published(self):
        time = timezone.now()
        self.forum.pub_date = time
        self.assertTrue(self.forum.was_published_recently())

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
        
    def test_with_forums(self):
        self.client.login(email='test@example.com',password='Secret1999')
        forum = PostModel.objects.create(title='Titulo random', thematic='Tematica', post_text='Post random de testeo', user=self.user)
        response = self.client.get(reverse('foros:Index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_posts"], [forum])
    
    def test_forum_from_inactive_user(self):
        second_user = CustomUser.objects.create_user(email='test2@example.com',nickname='test2user',password='Secret1999', is_active=False)
        PostModel.objects.create(title='Titulo random', thematic='Tematica', post_text='Post random de testeo', user=second_user)
        self.client.login(email='test@example.com',password='Secret1999')
        response=self.client.get(reverse('foros:Index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No posts are available')
        self.assertQuerysetEqual(response.context['latest_posts'], [])
    
    def test_forum_from_active_and_inactive_user(self):
        second_user = CustomUser.objects.create_user(email='test2@example.com',nickname='test2user',password='Secret1999', is_active=False)
        PostModel.objects.create(title='Titulo random', thematic='Tematica', post_text='Post random de testeo', user=second_user)
        activeforum=PostModel.objects.create(title='Titulo random', thematic='Tematica', post_text='Post random de testeo', user=self.user)
        self.client.login(email='test@example.com',password='Secret1999')
        response=self.client.get(reverse('foros:Index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_posts'], [activeforum])
    
class ForumDetailViewsTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@example.com',nickname='testuser',password='Secret1999')
        
    def test_no_comments_on_forum(self):
        forum = PostModel.objects.create(title='Titulo random', thematic='Tematica', post_text='Post random de testeo', user=self.user)
        response = self.client.get(reverse('foros:Foro_detalle', kwargs={'pk':forum.id}))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There  are no comments yet!')
    
    def test_no_thematic_forum(self):
        forum = PostModel.objects.create(title='Titulo random', post_text='Post random de testeo', user=self.user)
        response = self.client.get(reverse('foros:Foro_detalle', kwargs={'pk':forum.id}))
        
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, ' -- Thematic: ')
        
    def test_comment_from_inactive_user(self):
        forum = PostModel.objects.create(title='Titulo random', post_text='Post random de testeo', user=self.user)
        second_user = CustomUser.objects.create_user(email='test2@example.com',nickname='test2user',password='Secret1999', is_active=False)
        comment = CommentModel.objects.create(user=second_user, post=forum, text_comment="Comentario de testeo")
        response = self.client.get(reverse('foros:Foro_detalle', kwargs={'pk':forum.id}))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "(Usuario Inactivo)")
        self.assertQuerysetEqual(response.context['postmodel'].commentmodel_set.all(), [comment])

    def test_comment_from_active_and_inactive_user(self):
        forum = PostModel.objects.create(title='Titulo random', post_text='Post random de testeo', user=self.user)
        second_user = CustomUser.objects.create_user(email='test2@example.com',nickname='test2user',password='Secret1999', is_active=False)
        first_comment = CommentModel.objects.create(user=second_user, post=forum, text_comment="Comentario de testeo")
        second_comment = CommentModel.objects.create(user=self.user, post=forum, text_comment="Comentario de testeo")
        response = self.client.get(reverse('foros:Foro_detalle', kwargs={'pk':forum.id}))
        
        c_list=list(response.context['postmodel'].commentmodel_set.all())
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "(Usuario Inactivo)")
        self.assertQuerysetEqual(c_list, [first_comment, second_comment])
