from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm
from .models import CustomUser
# Create your views here.
class SelfUserView(DetailView):
    template_name = 'profile/user_profile.html'
    
    def get_object(self):
        return self.request.user

class UserView(LoginRequiredMixin, DetailView):
    template_name = 'profile/user_profile.html'
    login_url = '/user/login/'
    
    def get_object(self):
        self.user=get_object_or_404(CustomUser,nickname = self.kwargs['nickname'])
        return self.user
        # return CustomUser.objects.get(nickname = self.kwargs['nickname'])

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('forum_profile:self-profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'profile/signup.html', {'form': form})
