from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Index"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("auth_status", views.auth_status, name="auth_status"),
    path("about", views.about, name="about"),
    path("account/subscribe", views.subscribe, name="subscribe"),
    path("account/unsubscribe", views.unsubscribe, name="unsubscribe"),
    path("geocode_access", views.geocode_access, name="geocode_access"),
    path("account", views.account, name="account")
]