from django.views.generic.list import ListView
from customer.models import Customer_Address, Customer
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from customer.forms import Customer_AddressForm, CustomerForm
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

class Customer_AddressMixin(object):
    model = Customer_Address
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Customer_Address'})
        return kwargs

class Customer_AddressFormMixin(Customer_AddressMixin):
    form_class = Customer_AddressForm
    template_name = 'customer/object_form.html'

class Customer_AddressList(Customer_AddressMixin, ListView):
    template_name = 'customer/object_list.html'

class Customer_AddressDetail(Customer_AddressMixin, DetailView):
    pass

class NewCustomer_Address(Customer_AddressFormMixin, CreateView):
    pass

class EditCustomer_Address(Customer_AddressFormMixin, UpdateView):
    pass

class DeleteCustomer_Address(Customer_Address, DeleteView):
    template_name = 'customer/object_confirm_delete.html'
    def get_success_url(self):
        return reverse('customer_address_list')

class CustomerMixin(object):
    model = Customer
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Customer'})
        return kwargs

class CustomerFormMixin(CustomerMixin):
    form_class = CustomerForm
    template_name = 'customer/object_form.html'

class CustomerList(CustomerMixin, ListView):
    template_name = 'customer/object_list.html'

class ViewCustomer(CustomerMixin, DetailView):
    pass

class NewCustomer(CustomerFormMixin, CreateView):
    pass

class EditCustomer(CustomerFormMixin, UpdateView):
    pass

class KillCustomer(CustomerMixin, DeleteView):
    template_name = 'customer/object_confirm_delete.html'
    def get_success_url(self):
        return reverse('customer_list')

class ViewCustomer_Address(CustomerMixin, ListView):
    template_name = 'customer/object_list.html'
    def get_queryset(self):
        self.customer_address = get_object_or_404(Customer_Address, slug=self.kwargs['slug'])
        return super(ViewCustomer_Address, self).get_queryset().filter(customer_address=self.customer_address)