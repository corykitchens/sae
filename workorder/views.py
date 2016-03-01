from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.contrib.auth.models import User

from .models import WorkOrder, ServiceType
from customer.models import Customer, Customer_Address as CustomerAddress
from vehicle.models import Vehicle
from employee.models import Employee

from .forms import  WorkOrderForm
from customer.forms import CustomerForm, AddressForm
from vehicle.forms import VehicleForm
# Create your views here.
def work_orders(request):
	work_orders = WorkOrder.objects.all()
	return render(request, 'workorder/work_order_list.html', {'work_orders' : work_orders})


def create_work_order(request):
	if request.method=='GET':
		# Get customer form
		customer_form = CustomerForm()
		ca_form = AddressForm()
		work_order_form = WorkOrderForm()
		vehicle_form = VehicleForm()
		return render(request, 'workorder/create_work_order.html', {'customer_form' : customer_form,
																	'ca_form': ca_form,
																	'vehicle_form' : vehicle_form,
																	'work_order_form' : work_order_form})

	elif request.method=='POST':
		if request.POST['c-first-name']  != '':
			# Returning Customer
			query_first_name = request.POST['c-first-name']
			query_last_name = request.POST['c-last-name']
			try:
				customer = Customer.objects.get(first_name=query_first_name, last_name=query_last_name)
				#Customer found
				return HttpResponse(customer)
				#Begin Vehicle
			except Customer.DoesNotExist:
				HttpResponse('Error querying customer')
		else:
		

			

			# New customer
			c = Customer()
			c.first_name = request.POST['first_name']
			c.middle_initial = request.POST['middle_initial']
			c.last_name  = request.POST['last_name']
			c.email =	request.POST['email']


			# Customer Address
			ca = CustomerAddress()
			ca.address = request.POST['address']
			ca.city	= request.POST['city']
			ca.state = request.POST['state']
			ca.save()
			c.address = ca
			c.save()
			
			# Vehicle
			v = Vehicle()
			v.license_plate = request.POST['license_plate']
			v.make	= request.POST['make']
			v.model = request.POST['model']
			v.vin	= request.POST['vin']
			v.year = request.POST['year']
			v.save()
			c.vehicle.add(v)

			w = WorkOrder()
			w.odometer = request.POST['odometer']
			w.date_created = timezone.now()
			w.problem_description = request.POST['problem_description']
			w.estimate_initial = request.POST['estimate_initial']
			w.customer = c
		
			w.vehicle = v
			w.employee = Employee.objects.get(first_name='Ned', last_name='Stark')

			service_list = request.POST.getlist('service_type')
			w.save()
			work_orders = WorkOrder.objects.all()
			employee = Employee.objects.get(user=request.user)
			return render(request, 'employee/employee_home.html', {'user': request.user, 'employee': employee,
				 'work_orders' : work_orders})




