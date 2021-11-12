from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	# required defaults to true
	email = forms.EmailField()

	class Meta:
		# telling the form which model it's interacting with
		model = User
		# telling the form which fields the form is going to display, in order
		fields = ['username', 'email', 'password1', 'password2']