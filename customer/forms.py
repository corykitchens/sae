from django import forms
from customer.models import Customer, Customer_Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Customer_Address
        fields = ('address', 'city', 'state')
        widgets = {
            'address' : forms.TextInput(attrs={'class' : 'form-control'}),
            'city': forms.TextInput(attrs={'class' : 'form-control'}),
            'state':  forms.TextInput(attrs={'class' : 'form-control'}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'middle_initial', 'last_name', 'email')
        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'middle_initial' : forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

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