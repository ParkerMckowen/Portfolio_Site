from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

'''
Register View
	- handles if the user is trying to view the page initially(GET) or if they are trying to submit
	  information (POST)
	- 
'''
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()

			# This part here is how you access data from the form
			username = form.cleaned_data.get('username')

			# Outputting a success message
			messages.success(request, f"Account created for {username}")

			#Redirecting the user to the login page once account is created
			return redirect('landing:landing-home')

	# When the user is loading the page/form
	else:
		# Creating a blank form, vs in the POST version we load the data the user entered
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form' : form})