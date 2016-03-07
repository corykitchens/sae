from django import forms
from django.forms import ModelForm
from vehicle.models import Vehicle


class VehicleForm(ModelForm):
	class Meta:
		model = Vehicle
		fields = ['license_plate', 'make', 'model',
				'vin', 'year']
		widgets = {
		    'license_plate' : forms.TextInput(attrs={'class' : 'form-control'}),
		    'make': forms.TextInput(attrs={'class' : 'form-control'}),
		    'model':  forms.TextInput(attrs={'class' : 'form-control'}),
		    'vin':  forms.TextInput(attrs={'class' : 'form-control'}),
		    'year':  forms.NumberInput(attrs={'class' : 'form-control'}),
		}
