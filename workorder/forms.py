from django.forms import ModelForm
from .models import WorkOrder

class WorkOrderForm(ModelForm):
	class Meta:
		model = WorkOrder
		fields = ['odometer',
				'problem_description', 'service_type',
				'estimate_initial',
				'parts_require']
