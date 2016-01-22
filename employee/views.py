from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from employee.models import Employee

# Create your views here.
class EmployeeDirectory(ListView):
	model = Employee
	context_object_name = "employees"