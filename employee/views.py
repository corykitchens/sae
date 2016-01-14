from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def employee_index(request):
	return HttpResponse('Employees')