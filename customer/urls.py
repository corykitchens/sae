from django.conf.urls import url
from customer.views import CustomerDirectory, customer_profile
from . import views
urlpatterns = [
	#landing page
	url(r'^customer_directory', CustomerDirectory.as_view(), name="customer_index"),
	url(r'^edit_profile/(?P<customer_id>[0-9])$', customer_profile, name="customer_profile")
	# r'^ <- begin of raw string
	# $' <- end of raw string
	#url(r'^(?P<test>[a-z]{2})$', views.a)



]