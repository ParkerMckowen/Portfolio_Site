from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "users"

urlpatterns = [
	path('register', views.register, name='users-registration'),
	path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
	path('logout', auth_views.LoginView.as_view(template_name='users/logout.html'), name='users-logout'),
]