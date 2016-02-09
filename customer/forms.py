from django import forms
from customer.models import Customer, Customer_Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Customer_Address
        fields = ('address', 'city', 'state')

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'middle_initial', 'last_name', 'email')

class Customer_Edit_Form(forms.ModelForm):
	class Meta:
		model  = Customer
		fields = ('email',		)

class Address_Edit_Form(forms.ModelForm):
	class Meta:
		model  = Customer_Address
		fields = ('address', 'city', 'state' )