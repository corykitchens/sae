from django import forms
from django.forms import ModelForm
from .models import WorkOrder

class WorkOrderForm(ModelForm):
		class Meta:
			model = WorkOrder
			fields = ['odometer',
					'problem_description', 'service_type',
					'parts_require']
			widgets = {
				'odometer' : forms.NumberInput(attrs={'class' : 'form-control'}),
				'problem_description' : forms.Textarea(attrs={'class' : 'form-control'}),
				'service_type' : forms.SelectMultiple(attrs={'class' : 'form-control'}),
				'parts_require' : forms.TextInput(attrs={'class' : 'form-control'}),
			}
