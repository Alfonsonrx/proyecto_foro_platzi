from django.db import models
from forum_profile.models import UsersModel

# Create your models here.
class PostModel(models.Model):
    
    id = models.UUIDField(primary_key=True, unique=True)
    title = models.CharField(max_length=200)
    thematic = models.CharField(max_length=24, blank=True, null=True)
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.title
    
class CommentModel(models.Model):
    
    id = models.UUIDField(primary_key=True, unique=True)
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    original_comment = models.ForeignKey("CommentModel", on_delete=models.CASCADE, blank=True, null=True)
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now_add=True)
    text_comment = models.TextField(max_length=500)
    
    def __str__(self):
        return self.text_comment