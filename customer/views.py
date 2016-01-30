from django.shortcuts import render
from django.views.generic import ListView

from customer.models import Customer

# Create your views here.
class CustomerDirectory(ListView):
	model = Customer
	context_object_name = "customer"
	