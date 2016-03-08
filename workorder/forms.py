from django import forms
from django.forms import ModelForm
from .models import WorkOrder, EmployeeServiceNotes

class WorkOrderForm(ModelForm):
		class Meta:
			model = WorkOrder
			fields = ['odometer',
					'problem_description', 'service_type',
					'parts_required']
			widgets = {
				'odometer' : forms.NumberInput(attrs={'class' : 'form-control'}),
				'problem_description' : forms.Textarea(attrs={'class' : 'form-control'}),
				'service_type' : forms.SelectMultiple(attrs={'class' : 'form-control'}),
				'parts_require' : forms.TextInput(attrs={'class' : 'form-control'}),
			}


class EmployeeServiceNotesForm(ModelForm):
	class Meta:
		model = EmployeeServiceNotes
		fields = ['date_serviced',
				'hours_spent','notes',
				'parts_used']
		widgets = {
			'date_serviced' : forms.DateTimeInput(attrs={'class' : 'form-control'}),
			'hours_spent' : forms.NumberInput(attrs={'class' : 'form-control'}),
			'notes' : forms.Textarea(attrs={'class' : 'form-control'}),
			'parts_used' : forms.SelectMultiple(attrs={'class' : 'form-control'}),
		}