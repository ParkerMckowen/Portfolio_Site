from django.shortcuts import render


# Create your views here.
def home(request):
	current_user = request.user
	if current_user is None:
		current_user = "Login Please"

	return render(request, 'landing/landing.html', {'user' : current_user})


