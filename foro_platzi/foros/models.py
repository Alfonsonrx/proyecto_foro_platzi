import uuid
import datetime
import pytz

from django.db import models
from forum_profile.models import CustomUser
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class PostModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    title = models.CharField(max_length=200)
    thematic = models.CharField(max_length=24, blank=True, null=True)
    post_text = models.TextField(max_length=1000, default=None)
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.title
    
    # ...
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        pub = self.pub_date
        datetime_pub = datetime.datetime(pub.year, pub.month, pub.day, 0, 0, tzinfo=pytz.utc)
        return now - datetime.timedelta(days=1) <= datetime_pub <= now
    
    # ...
    @admin.display(
        ordering='user',
        description='Author user',
    )
    def get_user_nick(self):
        return self.user.nickname
    
class CommentModel(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    original_comment = models.ForeignKey("CommentModel", on_delete=models.CASCADE, blank=True, null=True)
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now_add=True)
    text_comment = models.TextField(max_length=500)
    
    def __str__(self) -> str:
        return self.text_comment[:30]