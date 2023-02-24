from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormMixin
from django.views import generic
from django.utils import timezone
from django.urls import reverse

from .models import PostModel
from .forms import CommentForm

# Create your views here.
class IndexView(generic.ListView):
    # model = PostModel
    template_name = "foros/index.html"
    context_object_name = "latest_posts"
    
    def get_queryset(self):
        return PostModel.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]

class ForumView(generic.DetailView):
    model = PostModel
    template_name = 'foros/forum.html'
    
    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    