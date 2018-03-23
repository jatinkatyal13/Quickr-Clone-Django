from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^logout/?$', views.logout_view, name='logout'),
	url(r'^addProduct/?$', views.addProduct, name='add_product'),
	url(r'^browseProducts/?$', views.browseProducts, name='browse_products'),
	url(r'^requests/?$', views.requests, name='requests'),
	url(r'^myProducts/?$', views.myProducts, name='my_products'),
	url(r'^soldProducts/?$', views.soldProducts, name='sold_products'),
	url(r'^buy/(?P<id>[0-9]+)?$', views.buy, name='buy'),
	url(r'^acceptTrade/(?P<id>[0-9]+)?$', views.acceptTrade, name='accept_trade'),
	url(r'^declineTrade/(?P<id>[0-9]+)?$', views.declineTrade, name='decline_trade'),
	url(r'^buy/(?P<id>[0-9]+)?$', views.buy, name='buy'),
]
