from django import forms
from django.forms import ModelForm
from .models import WorkOrder

class WorkOrderForm(ModelForm):
<<<<<<< HEAD
        class Meta:
               model = WorkOrder
               fields = ['odometer',
                               'problem_description', 'service_type',
                               'estimate_initial', 'estimate_revision', 'hours_required',
                               'parts_require', 'estimate_approval', 'approval_date_time', 'amount_paid',
                               'date_completed']
=======
		class Meta:
			model = WorkOrder
			fields = ['odometer',
					'problem_description', 'service_type',
					'estimate_initial',
					'parts_require']
			widgets = {
				'odometer' : forms.NumberInput(attrs={'class' : 'form-control'}),
				'problem_description' : forms.Textarea(attrs={'class' : 'form-control'}),
				'service_type' : forms.SelectMultiple(attrs={'class' : 'form-control'}),
				'estimate_initial' : forms.NumberInput(attrs={'class' : 'form-control'}),
				'parts_require' : forms.TextInput(attrs={'class' : 'form-control'}),
			}
>>>>>>> 1f356d3f7aaa7fbd98b5990ca3e1120301039119
