from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.files import File
import os

from .models import Upload

@receiver(post_save, sender=Upload)
def extract_upload_text(sender, instance, created, **kwargs):
	if created:
		upload_obj = instance.file_name
		upload_path = upload_obj.path

		with open(upload_path,'r') as f:
			data = f.read()
			# Extract the data from whatever type of file

		print(data)
		
		f.close()
		