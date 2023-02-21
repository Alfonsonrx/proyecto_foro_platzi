from django.db import models

# Create your models here.
class UsersModel(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True, primary_key=True)
    description = models.TextField(blank=True, null=True)
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.nickname