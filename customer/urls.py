from django.conf.urls import url
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from customer.views import CustomerDirectory, add, customer_profile, edit #, AddressDirectory, add_address#, address_profile
from . import views

app_name="customers"

urlpatterns = [
	#landing page
	url(r'^customer_directory', CustomerDirectory.as_view(), name="customer_index"),
	url(r'^customer_form', add, name="customer_form"),
	url(r'^customer_profile/(?P<customer_id>[0-9]+)$', customer_profile, name="customer_profile"),
	url(r'^customer_edit_form/(?P<customer_id>[0-9]+)$', edit, name="customer_edit_form")
	#url(r'^address_form', add_address, name="address_form"),
	#url(r'^address_profile/(?P<address_id>[0-9])$', address_profile, name="address_profile")
]