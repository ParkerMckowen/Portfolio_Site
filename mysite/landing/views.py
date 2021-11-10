from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadForm

# Create your views here.
def home(request):
	return render(request, 'landing/landing.html')

def fileUpload(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponse("File Uploaded")
	else:
		form = UploadForm()

	return render(request, "landing/upload.html", {"form" : form})
