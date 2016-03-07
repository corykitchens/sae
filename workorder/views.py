from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.contrib.auth.models import User
from reportlab.pdfgen import canvas

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

def work_order_detail(request, work_order_id):
	try:
		w = WorkOrder.objects.get(pk=int(work_order_id))
	except WorkOrder.ObjectDoesNotExist:
		return HttpResponse('Error')
	return render(request, 'workorder/work_order_detail.html', {'work_order' : w})


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

			query_vehicle = int(request.POST['vehicle_id'])
			query_first_name = request.POST['first_name']
			query_last_name = request.POST['last_name']


			try:
				v = Vehicle.objects.get(pk=query_vehicle)
			except Vehicle.DoesNotExist:
				HttpResponse('Error querying vehicle')

			try:
				c = Customer.objects.get(first_name=query_first_name, last_name=query_last_name)
			except Customer.DoesNotExist:
				HttpResponse('Error querying customer')

			w = WorkOrder()
			w.odometer = request.POST['odometer']
			w.date_created = timezone.now()
			w.problem_description = request.POST['problem_description']
			w.estimate_initial = 0
			w.customer = c
			
			w.vehicle = v
			w.employee = Employee.objects.get(user=request.user)
			w.save()
			
			service_list = request.POST.getlist('service_type')
			for service in service_list:
				selected_service = ServiceType.objects.get(pk=int(service))
				w.service_type.add(selected_service)
				w.estimate_initial = w.estimate_initial + selected_service.cost
			w.save()

			work_orders = WorkOrder.objects.filter(employee=w.employee)
			employee = Employee.objects.get(user=request.user)
			
			return render(request, 'employee/employee_home.html', {'user': request.user, 'employee': employee,
				 'work_orders' : work_orders})
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

			# Work Order
			w = WorkOrder()
			w.odometer = request.POST['odometer']
			w.date_created = timezone.now()
			w.problem_description = request.POST['problem_description']
			w.estimate_initial = request.POST['estimate_initial']
			w.customer = c
		
			w.vehicle = v
			w.employee = Employee.objects.get(user=request.user)

			service_list = request.POST.getlist('service_type')
			w.save()
			work_orders = WorkOrder.objects.all()
			employee = Employee.objects.get(user=request.user)
			return render(request, 'employee/employee_home.html', {'user': request.user, 'employee': employee,
<<<<<<< HEAD
				 'work_orders' : work_orders})
=======
				 'work_orders' : work_orders})


def generate_customer_receipt(customer, vehicle, work_order, employee):
	####
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

	
	generateCustomerReceipt(c,v,w,e)
	cv = canvas.Canvas(response)
	
	cv.drawString(50,800, 'Customer Name : ')
	cv.drawString(100, 800, str(c))


	cv.save()
	cv.showPage()
	###
	return response


>>>>>>> 926ca9f9960b02a6e5d9bd7fb352b44f226cea67
