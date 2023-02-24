from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'foros'
urlpatterns = [
    path("", login_required(views.IndexView.as_view()), name="Index"),
    path("foro/<uuid:pk>/", login_required(views.ForumView.as_view()), name="Foro_detalle"),
]