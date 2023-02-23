from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView

from .forms import CustomUserCreationForm

# Create your views here.
class UserView(DetailView):
    template_name = 'profile/user_profile.html'
    
    def get_object(self):
        return self.request.user

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
            return redirect('forum_profile:profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'profile/signup.html', {'form': form})
