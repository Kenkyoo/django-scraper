from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import home, save_favorite

urlpatterns = [
    path("", home, name="home"),
    path("registro/", views.registro, name="registro"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("favorite/", save_favorite, name="save_favorite"),
]
