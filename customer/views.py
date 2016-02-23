from __future__ import print_function
import sys
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from customer.forms import CustomerForm, AddressForm, Customer_Edit_Form, Address_Edit_Form
from customer.models import Customer, Customer_Address
from vehicle.models import Vehicle
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

def edit(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    Customer_EditFormSet = formset_factory(Customer_Edit_Form, extra=1, min_num=0,validate_min=True)
    if request.method == 'POST':
        address_edit_form = Address_Edit_Form(request.POST)
        customer_edit_form = Customer_EditFormSet(request.POST)
        if all([customer_edit_form.is_valid(), address_edit_form.is_valid()]):
            address = address_edit_form.save()
            for inline_form in customer_edit_form:
                if inline_form.cleaned_data:
                    customer.address = address
                    customer.save()
            return redirect('/customers/customer_directory', {})
    else:
        form = Address_Edit_Form()
        formset = Customer_EditFormSet()

    return render(request, 'customer/customer_edit_form.html', {'formset': formset, 'form': form})




def get_customer(request, first_name, last_name):
    try:
        customer = Customer.objects.get(first_name=first_name.capitalize(), last_name=last_name.capitalize())
    except Customer.DoesNotExist:
        return HttpResponse(json.dumps({'msg' : 'Error querying customer' + first_name + " " + last_name}))

    response_data = {}
    response_data['customer_fn'] = customer.first_name
    response_data['customer_ln'] = customer.last_name
    response_data['customer_mi'] = customer.middle_initial
    response_data['customer_address'] = customer.address.address
    response_data['customer_city'] = customer.address.city
    response_data['customer_state'] = customer.address.state
    response_data['customer_zip_code'] = customer.address.zip_code

    try:
        vehicle = customer.vehicle.all() 
    except Vehicle.DoesNotExist:
        response_data['customer_vehicles'] = ''

    if vehicle:
        for i in range(0, len(vehicle)):
            response_data['vehicle'+str(i)] = str(vehicle[i])


    return HttpResponse(json.dumps(response_data),
            content_type="application/json"
)