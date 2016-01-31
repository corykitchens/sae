from django.conf.urls import patterns, url, include
from customer.views import CustomerDirectory,  customer_profile, CustomerList, ViewCustomer, NewCustomer, KillAddress,\
    EditCustomer
from . import views
urlpatterns = [
	#landing page
	url(r'^customer_directory', CustomerDirectory.as_view(), name="customer_index"),
	url(r'^(?P<slug>[\w-]+).customer/', include(customer_urls)),
	url(r'^NewCustomer$', NewCustomer.as_view(), name='customer_add'),
	url(r'^edit_profile/(?P<customer_id>[0-9])$', customer_profile, name="customer_profile"),
	# r'^ <- begin of raw string
	# $' <- end of raw string
	#url(r'^(?P<test>[a-z]{2})$', views.a)



]