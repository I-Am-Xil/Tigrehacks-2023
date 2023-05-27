from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Index"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("auth_status", views.auth_status, name="auth_status"),
    path("account", views.account, name="account"),
    path("about", views.about, name="about")
]