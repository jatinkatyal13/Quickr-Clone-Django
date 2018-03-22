from django import forms
from .models import *

class LoginForm(forms.Form):
	user = forms.CharField(max_length = 100)
	password = forms.CharField(widget = forms.PasswordInput)

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		exclude = ('owner',)
		widgets = {
			'date' : forms.SelectDateWidget(),
			'description' : forms.Textarea(attrs = { 'class': 'materialize-textarea' })
		}
