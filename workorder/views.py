from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView

from .models import WorkOrder
from .forms import  WorkOrderForm
from customer.forms import CustomerForm, AddressForm
from vehicle.forms import VehicleForm
# Create your views here.
def work_orders(request):
	return render(request, 'workorder/work_order_list.html', {})


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
