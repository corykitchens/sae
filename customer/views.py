from __future__ import print_function
import sys


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from customer.forms import CustomerForm, AddressForm
from customer.models import Customer, Customer_Address

# Create your views here.
#Publisher.objects.filter(name__contains="press") --- How to filter objects by a string regardless of length
class CustomerDirectory(ListView):
    model = Customer
    context_object_name = "customers"

# choice has the foreign key choice is customer poll is address
def add(request):
    CustomerFormSet = formset_factory(CustomerForm, extra=1, min_num=0,validate_min=True)
    if request.method == 'POST':
        customer_address_form = AddressForm(request.POST)
        customer_form = CustomerFormSet(request.POST)

        if all([customer_form.is_valid(), customer_address_form.is_valid()]):
            address = customer_address_form.save()
            for inline_form in customer_form:
                if inline_form.cleaned_data:
                    customer = inline_form.save(commit=False)
                    customer.address = address
                    customer.save()
            return redirect('customer_directory.html', {})
    else:
        form = AddressForm()
        formset = CustomerFormSet()

    return render(request, 'customer/customer_form.html', {'formset': formset, 'form': form})

def customer_profile(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    return render(request, 'customer/customer_profile.html', {'customer': customer})

def print_objs(*objs):
    print("OUTPUT->", objs, file=sys.stderr)