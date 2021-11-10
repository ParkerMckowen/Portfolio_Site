from django.forms import ModelForm
from .models import PDFModel

class UploadForm(ModelForm):
	class Meta:
		model = PDFModel
		fields = ('title', 'pdf')