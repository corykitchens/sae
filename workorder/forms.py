from django.forms import ModelForm
from .models import WorkOrder

class WorkOrderForm(ModelForm):
	class Meta:
		model = WorkOrder
		fields = ['customer', 'vehicle', 'employee', 'odometer',
				'date_created', 'problem_description', 'service_type',
				'estimate_initial', 'estimate_revision', 'hours_required',
				'parts_require', 'estimate_approval', 'approval_date_time', 'amount_paid',
				'date_completed']
