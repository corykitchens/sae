from django.conf.urls import url

from customer.views import CustomerDirectory

urlpatterns = [
	url(r'^', CustomerDirectory.as_view(), name="customer_index")
]