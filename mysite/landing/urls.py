from django.urls import path, include
from . import views

app_name = "landing"

urlpatterns = [
	path('', views.home, name = 'landing-home'),
]