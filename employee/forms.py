from django.forms import ModelForm
from employee.models import Employee, EmployeeAddress

class NewHireForm(ModelForm):
	class Meta:
		model = Employee
		fields = ['ssn', 'first_name', 'middle_initial', 
		'last_name', 'email', 'job_title', 'wage', 'birthdate',
		'sex']

class NewHireAddressForm(ModelForm):
	class Meta:
		model = EmployeeAddress
		fields = ['address', 'city', 'state', 'zip_code']