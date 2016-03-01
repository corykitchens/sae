import sys

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from employee.models import Employee
from announcement.models import Announcement
from workorder.models import WorkOrder
# Create your views here.
def login(request):
	
	if request.user.is_authenticated():
		try:
			employee = Employee.objects.get(user=request.user)
		except Employee.DoesNotExist:
			return render(request, 'login/login.html', {"error": "Error Employee information not found"})
		announcements = Announcement.objects.all()
		work_orders = WorkOrder.objects.all()
		return render(request, 'employee/employee_home.html', {'user': request.user, 'employee': employee,
			'announcements' : announcements, 'work_orders' : work_orders})
	
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				employee = Employee.objects.get(user=user)
				announcements = Announcement.objects.all()
				work_orders = WorkOrder.objects.all()
				return render(request, 'employee/employee_home.html', {'user': request.user, 'employee': employee,
					'announcements' : announcements, 'work_orders' : work_orders})
			else:
				return render(request, 'login/login.html', {"error": "Error unable to begin user session"})
		else:
			return render(request, 'login/login.html', {"error": "Error unable to authenticate user"})
	else:
		return render(request, 'login/login.html', {})


def logout(request):
	auth_logout(request)
	return render(request, 'login/login.html', {'message': 'Logout Successfull'})