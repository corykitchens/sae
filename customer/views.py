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
    if request.method == 'POST':
            #
            # process your form
            #address.customerid = c.id 
            #print c.first_name
            ID = request.session('c')
            customer = Customer.objects.get(id=ID)
            form = AddressForm(request.POST)
            if form.is_valid():
                form.save()
                ca = Customer.objects.get(address=request.POST['address'])
                customer.address = ca
                customer.save()

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
                c = Customer.objects.get(last_name=request.POST['last_name'])
                #print c.id
                request.session['c'] = c.id

                return redirect('/customers/address_form', {'customer': c})
            else:
                messages.error(request, "Error")
    return render(request, 'customer/customer_form.html', {'form': CustomerForm()})

def customer_profile(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    return render(request, 'customer/customer_profile.html', {'customer': customer})


