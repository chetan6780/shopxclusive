from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import views as authentication_view

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/',authentication_view.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',authentication_view.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',views.profile, name='profile')
]
