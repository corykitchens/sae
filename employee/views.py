from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import NewHireForm

from employee.models import Employee

# Create your views here.
class EmployeeDirectory(ListView):
	model = Employee
	context_object_name = "employees"


def employee_profile(request, employee_id):
	employee = Employee.objects.get(id=employee_id)
	return render(request, 'employee/employee_profile.html', {'employee': employee})

def hr_home(request):
	return render(request, 'employee/hr_home.html', {})

def new_hire(request):
	if request.method=='GET':
		new_hire_form = NewHireForm()
		return render(request, 'employee/hr_new_hire.html', {'new_hire_form' : new_hire_form})
	else:
		return HttpResponse('POST')