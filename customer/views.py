import sys
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from customer.forms import CustomerForm, AddressForm
from customer.models import Customer, Customer_Address

# Create your views here.
#Publisher.objects.filter(name__contains="press") --- How to filter objects by a string regardless of length
class AddressDirectory(ListView):
    model = Customer_Address
    model = Customer
    context_object_name = "address"


def add_address(request):
    print >>sys.stderr, 'inside add address'
    if request.method == 'POST':
            form = AddressForm(request.POST)
            print >>sys.stderr, request.POST

            if form.is_valid():
                form.save()

                return redirect('/customers/customer_directory')
            else:
                messages.error(request, "Error")
    return render(request, 'customer/address_form.html', {'form': AddressForm()})

class CustomerDirectory(ListView):
    model = Customer
    context_object_name = "customers"


def add(request):
    if request.method == 'POST':
            
            form = CustomerForm(request.POST)
            if form.is_valid():
                form.save()
                customer = Customer.objects.get(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
                print >>sys.stderr, customer
                #Customer.objects.filter(last_name=request.POST['last_name'])
                return render(request, 'customer/address_form.html', {'customer': customer, 'form': AddressForm()})
            else:
                messages.error(request, "Error")
    return render(request, 'customer/customer_form.html', {'form': CustomerForm()})

def customer_profile(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    return render(request, 'customer/customer_profile.html', {'customer': customer})
