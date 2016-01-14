from django.shortcuts import render
from django.views.generic import ListView

from employee.models import Employee

# Create your views here.
class EmployeeDirectory(ListView):
	model = Employee
	