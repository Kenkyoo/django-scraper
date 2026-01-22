from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import delete_all_favorites, delete_favorite, favorites, home, save_favorite

urlpatterns = [
    path("", home, name="home"),
    path("register/", views.registro, name="register"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("favorite/", save_favorite, name="save_favorite"),
    path("delete/", delete_favorite, name="delete_favorite"),
    path("delete-all-favorites/", delete_all_favorites, name="delete_all_favorites"),
    path("favorites/", favorites, name="favorites"),
]
