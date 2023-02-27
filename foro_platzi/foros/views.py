from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin
from django.views import generic, View
from django.utils import timezone
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PostModel,CommentModel
from .forms import CommentForm, ForumForm

# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/user/login/'
    template_name = "foros/index.html"
    context_object_name = "latest_posts"
    
    def get_queryset(self):
        return PostModel.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]

"""
Comment Upload and Forum Details View
"""
class ForumGetView(generic.DetailView):
    model = PostModel
    template_name = 'foros/forum.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class CommentPostView(SingleObjectMixin,FormView):
    
    template_name = 'foros/forum.html'
    form_class = CommentForm
    model = CommentModel
    success_url = '#'
    success_message = "Your Comment has been submitted"
    
    def post(self, request, *args, **kwargs):
        """
        Posts the comment only if the user is logged in.
        """
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        # self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
class ForumView(View):

    def get(self, request, *args, **kwargs):
        view = ForumGetView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('forum_profile:login'))
        view = CommentPostView.as_view()
        form = CommentForm(request.POST)
        form.instance.user = request.user
        form.instance.post = PostModel.objects.get(id=self.kwargs['pk'])
        if form.is_valid():
            form.save()
        # return redirect(reverse('foros:Foro_detalle',kwargs={'pk':self.kwargs['pk']}))
        return view(request,*args, **kwargs)

def insert_forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            forum = form.save()
            # return redirect('foros:Index')
            return redirect(reverse('foros:Foro_detalle', kwargs={'pk':forum.id}))
    else:
        form = ForumForm()
    return render(request, 'foros/add_forum.html', {'form': form})