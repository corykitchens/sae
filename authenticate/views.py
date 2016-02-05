import sys

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from employee.models import Employee
from announcement.models import Announcement

# Create your views here.
def login(request):
	
	if request.user.is_authenticated():
		employee = Employee.objects.get(user=request.user)
		if not employee:
			return render(request, 'login/login.html', {"error": "Error querying employee"})
		announcements = Announcement.objects.all()
		return render(request, 'employee/employee_home.html', {'user': request.user, 'employee': employee,
			'announcements' : announcements})
	
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			
			if user.is_active:
				auth_login(request, user)
				employee = Employee.objects.get(user=user)
				announcements = Announcement.objects.all()
				return render(request, 'employee/employee_home.html', {'user': user, 'employee': employee,
					'announcements' : announcements})
			else:
				return HttpResponse("Could not login")
		else:
			return HttpResponse('Could not authenticate')
		# form = LoginUserForm(request.POST)

		# if form.is_valid():
		# 	return HttpResponse('Worked')
		# else:
		# 	return HttpResponse('Failed validity')
	else:
		#form = LoginUserForm()
		return render(request, 'login/login.html', {})


def logout(request):
	auth_logout(request)
	return render(request, 'login/login.html', {'message': 'Logout Successfull'})