from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "upload"

urlpatterns = [
	path('selection/', views.upload_file, name="upload-selection"),
	path('filelist/', views.list_files, name="upload-filelist"),
]