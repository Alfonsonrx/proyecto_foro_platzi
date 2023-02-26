from django.contrib import admin
from django import forms

from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name','nickname', 'now_active', 'time_active','date_joined')
    ordering = ['date_joined']
    date_hierarchy = 'date_joined'
    search_fields = ['email','name', 'nickname']

# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)