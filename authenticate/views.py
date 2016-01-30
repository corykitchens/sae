import sys
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login 
from employee.models import Employee

# Create your views here.
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			
			if user.is_active:
				auth_login(request, user)
				employee = Employee.objects.get(user=user)
				#print >>sys.stderr, employee
				return render(request, 'employee/employee_list.html', {'user': user, 'employee': employee})
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