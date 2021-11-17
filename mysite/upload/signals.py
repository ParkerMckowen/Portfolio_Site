from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from django.conf import settings
from django.core.files import File
import os
import pdfplumber

from .models import Upload

# @receiver(post_save, sender=Upload)
# def extract_upload_text(sender, instance, created, **kwargs):
# 	if created:
# 		upload_obj = instance.file_name
# 		upload_path = upload_obj.path

# 		text = ""

# 		with pdfplumber.open(upload_path) as pdf:
# 			print(pdf.metadata)
# 			for page in pdf.pages:
# 				extracted_text = page.extract_text()
# 				cleaned_text = ' '.join(extracted_text.split())
# 				text += cleaned_text
# 				page.close()
# 		pdf.close()

# 		instance.text = text



