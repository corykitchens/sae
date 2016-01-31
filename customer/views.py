from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from customer.models import Customer

# Create your views here.
class CustomerDirectory(ListView):
	model = Customer
	context_object_name = "customers"


def customer_profile(request, customer_id):
	Customer = Customer.objects.get(id=customer_id)
	return render(request, 'customers/customer_profile.html', {'customer': customer})
	