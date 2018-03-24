from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.ImageField(upload_to = 'main/static/pic_folder/', blank = False, null = True)
	date = models.DateField(default = timezone.now())
	owner = models.ForeignKey(User, on_delete = models.CASCADE)

class TradeRequest(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name="trade_request_product")
	receiver = models.ForeignKey(User, on_delete = models.CASCADE)

class Traded(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name="trade_product")
	receiver = models.ForeignKey(User, on_delete = models.CASCADE)
