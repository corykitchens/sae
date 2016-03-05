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

        def __init__(self, *args, **kwargs):
            super(CustomerForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs.update({'class' : 'form-control'})
            self.fields['last_name'].widget.attrs.update({'class' : 'form-control'})
            self.fields['middle_initial'].widget.attrs.update({'class' : 'form-control'})
            self.fields['email'].widget.attrs.update({'class' : 'form-control'})


class Customer_Edit_Form(forms.ModelForm):
	class Meta:
		model  = Customer
		fields = ('email',		)

class Address_Edit_Form(forms.ModelForm):
	class Meta:
		model  = Customer_Address
		fields = ('address', 'city', 'state' )