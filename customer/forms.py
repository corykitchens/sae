from django import forms
from customer.models import Customer, Customer_Address

class Customer_AddressForm(forms.ModelForm):
    class Meta:
        model = Customer_Address
        fields = ('address', 'city', 'state', 'zip_code')

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'middle_initial', 'last_name', 'email',)