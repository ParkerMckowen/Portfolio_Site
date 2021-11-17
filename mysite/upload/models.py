from django.db import models
from users.models import Profile
from django.contrib.auth.models import User

class Upload(models.Model):
	file_name = models.FileField(upload_to='pdfs')
	uploaded_at = models.DateTimeField(auto_now_add=True)
	activated = models.BooleanField(default=False)
	text = models.TextField(null=True)
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return f"File id: {self.id}"



'''
Example of a model for uploading documents

class Upload(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	pdf = models.FileField(upload_to='books/pdfs/')

	def __str__(self):
		return self.title
'''