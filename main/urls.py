from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^logout/?$', views.logout_view, name='logout'),
	url(r'^addProduct/?$', views.addProduct, name='add_product'),
	url(r'^browseProducts/?$', views.browseProducts, name='browse_products'),
	url(r'^requests/?$', views.requests, name='requests'),
	url(r'^buy/(?P<id>[0-9]+)?$', views.buy, name='buy'),
]
