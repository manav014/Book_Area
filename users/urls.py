from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

   # path('register/', views.register, name="register"),
   # path('login', views.login_request, name="login"),
    path("logout", views.handleLogout, name="handleLogout"),
    path('signup', views.handleSignup, name="handleSignup"),
    path('handleLogin', views.handleLogin, name="handleLogin"),
    path('login', views.login_form, name="login_form"),
    path('register/', views.register_form, name="register_form"),
]
