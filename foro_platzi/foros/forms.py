from django.forms import ModelForm
from .models import PostModel, CommentModel

class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['text_comment',]
        
class ForumForm(ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'thematic', 'post_text']