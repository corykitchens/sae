import sys

from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from employee.models import Employee
from announcement.models import Announcement
from workorder.models import WorkOrder
# Create your views here.
def login(request):
	if request.user.is_authenticated():
		emp_home_tmp = 'employee/employee_home.html'

		try:
			employee = Employee.objects.get(user=request.user)
		except Employee.DoesNotExist:
			return render(request, 'login/login.html', {"error": "Error Employee information not found"})

		if employee.job_title == "Administrative":
			emp_home_tmp = 'employee/hr_home.html'

		if employee.job_title == "Service Technician":
			try:
				work_orders = WorkOrder.objects.filter(employee=employee).exclude(status='Completed')
			except WorkOrder.DoesNotExist:
				return render(request, emp_home_tmp, {'employee' : employee, 'user' : request.user})
		else:
			try:
				work_orders = WorkOrder.objects.filter(Q(status__contains="Completed") | Q(status__contains="Awaiting Payment"))

			except WorkOrder.DoesNotExist:
				return render(request, emp_home_tmp, {'employee' : employee, 'user' : request.user})
		request.session['job_title'] = employee.job_title
		return render(request, emp_home_tmp, {'employee' : employee, 'user' : request.user, 'work_orders' : work_orders})
		
	'''
	Initial login
	'''
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		emp_home_tmp = 'employee/employee_home.html'
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				
				employee = Employee.objects.get(user=request.user)
				print >>sys.stderr, employee.job_title
				
				if employee.job_title == "Administrative":
					emp_home_tmp = 'employee/hr_home.html'
				
				if employee.job_title == "Service Technician":
					try:
						work_orders = WorkOrder.objects.filter(employee=employee).exclude(status='Completed')
					except WorkOrder.DoesNotExist:
						return render(request, emp_home_tmp, {'employee' : employee, 'user' : request.user})
				else:
					try:
						work_orders = WorkOrder.objects.filter(Q(status__contains="Completed") | Q(status__contains="Awaiting Payment"))
					except WorkOrder.DoesNotExist:
						return render(request, emp_home_tmp, {'employee' : employee, 'user' : request.user})
				request.session['job_title'] = employee.job_title
				return render(request, emp_home_tmp, {'user': request.user, 'employee': employee,
					'work_orders' : work_orders})
			else:
				return render(request, 'login/login.html', {"error": "Error unable to begin user session"})
		else:
			return render(request, 'login/login.html', {"error": "Error unable to authenticate user"})
	else:
		return render(request, 'login/login.html', {})


def logout(request):
	auth_logout(request)
	return render(request, 'login/login.html', {'message': 'Logout Successfull'})

