from django.db import models

# Create your models here.
class PDFModel(models.Model):
	title = models.CharField(max_length=50)
	pdf = models.FileField(upload_to='pdfs/')

	class Meta:
		ordering = ['title']

	def __str__(self):
		return f"{self.title}"