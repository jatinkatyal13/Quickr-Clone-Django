from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

@login_required
def requests(request):
	req = TradeRequest.objects.filter(product__owner = request.user)

	context = {
		'request' : req
	}
	return render(request, 'requests.html', context)

@login_required
def buy(request, id):
	TradeRequest.objects.create(product = Product.objects.get(id=id), receiver = request.user)
	return HttpResponseRedirect('/browseProducts')

def browseProducts(request):

	products = Product.objects.all()[:10]

	context = {
		'products' : products
	}
	return render(request, 'browseProduct.html', context)

@login_required
def addProduct(request):
	done = False 
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			obj = form.save(commit = False)
			obj.owner = request.user
			obj.save()
			form = ProductForm()
			done = True
	else:
		form = ProductForm()

	context = {
		'done' : done,
		'form' : form
	}
	return render(request, 'addProduct.html', context)

def index(request):
	errors = list()
	if request.method == "POST":
		if request.user.is_authenticated:
			return HttpResponseRedirect('/')
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

@login_required
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
