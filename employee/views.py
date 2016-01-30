from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from employee.models import Employee

# Create your views here.
class EmployeeDirectory(ListView):
	model = Employee
	context_object_name = "employees"


def employee_profile(request, employee_id):
	employee = Employee.objects.get(id=employee_id)
	return render(request, 'employee/employee_profile.html', {'employee': employee})