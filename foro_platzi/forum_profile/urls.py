from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'forum_profile'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='profile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/user/login'), name='logout'),
    path('profile/', login_required(views.SelfUserView.as_view()), name='self-profile'),
    path('profile/<str:nickname>', login_required(views.UserView.as_view()), name='profile'),
    path('signup/', views.signup, name='signup'),
]