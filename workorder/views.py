from django.shortcuts import render
from django.http import HttpResponse

from .forms import  WorkOrderForm
from customer.forms import CustomerForm, AddressForm
# Create your views here.
def create_work_order(request):
	if request.method == 'POST':
		return HttpResponse("Received form")
	else:
		customer_form = CustomerForm()
		customer_address_form = AddressForm()
		form = WorkOrderForm()

	return render(request, 'workorder/create_work_order.html', {'customer_form': customer_form, 'customer_address_form' : customer_address_form, 'form': form})