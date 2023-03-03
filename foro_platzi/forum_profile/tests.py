import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse
from django.contrib.auth import get_user

from .models import CustomUser

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@example.com',nickname='testuser',password='Secret1999')

    def test_recently_joined_past(self):
        time = timezone.now() + datetime.timedelta(days=-30)
        self.user.date_joined = time
        self.assertFalse(self.user.recently_joined())
    
    def test_recently_joined_past_success(self):
        time = timezone.now() + datetime.timedelta(days=-10)
        self.user.date_joined = time
        self.assertTrue(self.user.recently_joined())
    
    def test_recently_joined_now(self):
        time = timezone.now()
        self.user.date_joined = time
        self.assertTrue(self.user.recently_joined())
    
