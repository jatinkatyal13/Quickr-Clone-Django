from .models import *

def add_request_count(request):
	if request.user.is_authenticated:
		count = TradeRequest.objects.filter(product__in = request.user.product_set.all()).count()
	else:
		count = 0
	return {'count' : count}
