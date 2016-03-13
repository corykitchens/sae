import sys
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import NewHireForm, NewHireAddressForm


from employee.models import Employee
from workorder.models import WorkOrder
# Create your views here.
class EmployeeDirectory(ListView):
	model = Employee
	context_object_name = "employees"


def employee_profile(request, employee_id):
	user = request.user

	employee = Employee.objects.get(user=user)
	return render(request, 'employee/employee_profile.html', {'employee': employee})

def hr_view_pending(request):
	completed_work_orders = WorkOrder.objects.filter(status='Completed')
	payment_work_orders = WorkOrder.objects.filter(status='Awaiting Payment')


	return render(request, 'employee/hr_home.html', {'user' : request.user, 'completed_work_orders' : completed_work_orders, 'payment_work_orders' : payment_work_orders})

def new_hire(request):
	if request.method=='GET':
		new_hire_form = NewHireForm()
		new_hire_address_form = NewHireAddressForm()
		return render(request, 'employee/hr_new_hire.html', {'new_hire_form' : new_hire_form, 
			'new_hire_address_form' : new_hire_address_form})
	
	elif request.method=='POST':
		
		return HttpResponse('POST')


def change_password(request, employee, new_password):
	return HttpResponse('Change Passwordw')