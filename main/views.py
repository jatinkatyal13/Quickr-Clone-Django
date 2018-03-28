from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import *
from .models import *

@login_required
def soldProducts(request):
	products = Traded.objects.filter(product__owner = request.user)
	context = {
		'products' : products
	}
	return render(request, 'soldProducts.html', context)

@login_required
def myProducts(request):
	products = Traded.objects.filter(receiver = request.user)

	context = {
		'products' : products
	}
	return render(request, 'myProducts.html', context)

@login_required
def requests(request):
	req = TradeRequest.objects.filter(product__owner = request.user)

	context = {
		'requests' : req
	}
	return render(request, 'requests.html', context)

@login_required
def acceptTrade(request, id):
	request = TradeRequest.objects.get(id = id)
	Traded.objects.create(
		product = request.product,
		receiver = request.receiver
	)
	request.delete()
	return HttpResponseRedirect('/requests/')

@login_required
def declineTrade(request, id):
	request = TradeRequest.objects.get(id = id)
	request.delete()
	return HttpResponseRedirect('/requests/')

@login_required
def buy(request, id):
	TradeRequest.objects.create(product = Product.objects.get(id=id), receiver = request.user)
	return HttpResponseRedirect('/browseProducts')

def browseProducts(request):

	if request.user.is_authenticated:
		products = Product.objects.filter(~Q(owner = request.user) & Q(trade_request_product = None) & Q(trade_product = None))[:10]
	else:
		products = Product.objects.filter(Q(trade_request_product = None) & Q(trade_product = None))

	context = {
		'products' : products
	}
	return render(request, 'browseProduct.html', context)

@login_required
def addProduct(request):
	done = False 
	if request.method == "POST":
		form = ProductForm(request.POST, request.FILES)
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
