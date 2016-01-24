import sys
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginUserForm

# Create your views here.
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		print >>sys.stderr, user
		if user is not None:
			
			if user.is_active:
				
				#login(request, user)
				return render(request, 'employee/profile_home.html', {'user' : user})
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