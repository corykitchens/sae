from django.forms import ModelForm
from employee.models import Employee, Employee_Address

class NewHireForm(ModelForm):
	class Meta:
		model = Employee
		fields = ['ssn', 'first_name', 'middle_initial', 
		'last_name', 'email', 'job_title', 'wage', 'birthdate',
		'sex', 'user']
		

