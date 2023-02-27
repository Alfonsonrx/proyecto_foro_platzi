from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from django import forms

from .models import PostModel, CommentModel

class ComentsInline(admin.TabularInline):
    model = CommentModel
    extra=1
    # exclude=['id','original_comment']

class PostModelAdmin(admin.ModelAdmin):
    inlines = (ComentsInline,)
    list_display = ('id', 'title', 'thematic', 'get_user_nick', 'pub_date','was_published_recently')
    ordering = ['pub_date']
    date_hierarchy = 'pub_date'
    list_filter = ['pub_date']
    search_fields = ['title','thematic']

# Register your models here.
admin.site.register(PostModel,PostModelAdmin)
admin.site.register(CommentModel)
