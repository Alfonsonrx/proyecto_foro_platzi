import datetime

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib import admin

from .managers import CustomUserManager
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email address"), unique=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(_("Nickname"), max_length=100, unique=True, error_messages={"unique": _("A user with that nickname already exists."),})
    description = models.TextField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    # ...
    @admin.display(
        boolean=True,
        # ordering='pub_date',
        description='Active?',
    )
    def now_active(self):
        return self.is_active
    
    def recently_joined(self):
        now=timezone.now()
        return now - datetime.timedelta(days=-15) <= self.date_joined <= now
    
    def time_active(self):
        if self.is_active:
            now=timezone.now()
            delta = now - self.date_joined
            return "{} days active".format(delta.days)
        else:
            return "Is not active"