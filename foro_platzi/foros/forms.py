from django.forms import ModelForm
from .models import CommentModel

class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['text_comment',]