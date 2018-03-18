from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *

def index(request):

	errors = list()
	if request.method == "POST":
		loginForm = LoginForm(request.POST)
		if loginForm.is_valid():
			user = loginForm.cleaned_data['user']
			password = loginForm.cleaned_data['password']
			user = authenticate(username = user, password = password)

			if user is not None:
				login(request, user)
				try:
					return HttpResponseRedirect(request.GET['next'])
				except:
					return HttpResponseRedirect('/')
			else:
				errors.append("<span class='red-text'>Invalid Username or password</span>")
		else:
			errors.append(loginForm.errors)
	else:
		loginForm = LoginForm()
	context = {
		'errors' : errors,
		'LoginForm' : loginForm 
	}
	return render(request, 'index.html', context) 
