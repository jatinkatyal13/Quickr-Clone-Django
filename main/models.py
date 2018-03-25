from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

category_choice = [
	"Electronics",
	"HouseHold",
	"Daily",
	"Clothing",
]

class Product(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.ImageField(upload_to = 'main/static/pic_folder/', blank = False, null = True)
	category = models.IntegerField(choices = tuple([ x for x in enumerate(category_choice)]))
	date = models.DateField(default = timezone.now())
	owner = models.ForeignKey(User, on_delete = models.CASCADE)

	def getImagePath(self):
		return "/".join(self.image.name.split('/')[2:])

class TradeRequest(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name="trade_request_product")
	receiver = models.ForeignKey(User, on_delete = models.CASCADE)

class Traded(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name="trade_product")
	receiver = models.ForeignKey(User, on_delete = models.CASCADE)
