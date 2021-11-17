from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

from .forms import UploadForm
from .models import Upload

import pdfplumber

def extract_pdf(file):
	text = ""

	with pdfplumber.open(file) as pdf:
		print(pdf.metadata)
		for page in pdf.pages:
			extracted_text = page.extract_text()
			cleaned_text = ' '.join(extracted_text.split())
			text += cleaned_text
			page.close()
	pdf.close()

	return text

@login_required(login_url='users:users-login')
def upload_file(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			filepath = obj.file_name
			obj.text = extract_pdf(filepath)
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
