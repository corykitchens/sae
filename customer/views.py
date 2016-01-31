from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from customer.forms import AddressForm, CustomerForm

from customer.models import Customer, Customer_Address

# Create your views here.
class CustomerDirectory(ListView):
	model = Customer
	context_object_name = "customers"


def customer_profile(request, customer_id):
	Customer = Customer.objects.get(id=customer_id)
	return render(request, 'customers/customer_profile.html', {'customer': customer})

class CustomerMixin(object):
    model = Customer
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Customer'})
        return kwargs

class CustomerFormMixin(CustomerMixin):
    form_class = CustomerForm
    template_name = 'customers/object_form.html'

class CustomerList(CustomerMixin, ListView):
    template_name = 'customers/object_list.html'

class CustomerDetail(CustomerMixin, DetailView):
    pass

class NewCustomer(CustomerFormMixin, CreateView):
    pass

class EditCustomer(CustomerFormMixin, UpdateView):
    pass

class DeleteCustomer(CustomerMixin, DeleteView):
    template_name = 'customers/object_confirm_delete.html'
    def get_success_url(self):
        return reverse('customer_list')

class AddressMixin(object):
    model = Customer_Address
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Address'})
        return kwargs

class AddressFormMixin(AddressMixin):
    form_class = AddressForm
    template_name = 'customers/object_form.html'

class PeopleList(AddressMixin, ListView):
    template_name = 'customers/object_list.html'

class ViewAddress(AddressMixin, DetailView):
    pass

class NewAddress(AddressFormMixin, CreateView):
    pass

class EditAddress(AddressFormMixin, UpdateView):
    pass

class KillAddress(AddressMixin, DeleteView):
    template_name = 'customers/object_confirm_delete.html'
    def get_success_url(self):
        return reverse('customer_list')

class ViewCustomer(AddressMixin, ListView):
    template_name = 'customers/object_list.html'
    def get_queryset(self):
        self.customer = get_object_or_404(Customer, slug=self.kwargs['slug'])
        return super(ViewCustomer, self).get_queryset().filter(customer=self.customer)
    pass