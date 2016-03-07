from django.conf.urls import url
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from customer.views import CustomerDirectory, add, customer_profile, edit, vehicle_profile #, AddressDirectory, add_address#, address_profile
from . import views

app_name="customers"

urlpatterns = [
	#landing page
	url(r'^customer_directory', CustomerDirectory.as_view(), name="customer_index"),
	url(r'^customer_form', add, name="customer_form"),
	url(r'^customer_profile/(?P<customer_id>[0-9]+)$', customer_profile, name="customer_profile"),
	url(r'^vehicle_profile/(?P<vehicle_id>[0-9]+)$', vehicle_profile, name="vehicle_profile"),
	url(r'^customer_edit_form/(?P<customer_id>[0-9]+)$', edit, name="customer_edit_form"),
	url(r'^get_customer/(?P<first_name>[a-zA-Z]+)/(?P<last_name>[a-zA-Z]+)/$', views.get_customer)
	
]