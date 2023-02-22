from django.shortcuts import render, get_object_or_404
from .models import PostModel
from django.views import generic
from django.utils import timezone

# Create your views here.
class IndexView(generic.ListView):
    # model = PostModel
    template_name = "foros/index.html"
    context_object_name = "latest_posts"
    
    def get_queryset(self):
        return PostModel.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]
