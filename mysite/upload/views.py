from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

from .forms import UploadForm
from .models import Upload

import pdfminer
# Create your views here.

# VERY BASIC FILE UPLOAD METHOD
# def fileUpload(request):
# 	if request.method == 'POST':
# 		uploaded_file = request.FILES['document']
# 		fs = FileSystemStorage()
# 		fs.save(uploaded_file.name, uploaded_file)
# 	return render(request, "upload/uploadselection.html")


# def handle_file(file):
# 	with open(file.file_name.path, 'r') as f:
# 		text = pdfminer.high_level.extract_text(f)
# 		print(text)

@login_required(login_url='users:users-login')
def upload_file(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()

			return redirect('upload:upload-filelist')

	else:
		form = UploadForm()

	return render(request, 'upload/upload_file.html', {"form" : form})

@login_required(login_url='users:users-login')
def list_files(request):
	current_user = request.user
	uploads = Upload.objects.filter(user=current_user)
	return render(request, 'upload/list_file.html', {'uploads' : uploads})
