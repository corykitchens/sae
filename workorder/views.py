from django.shortcuts import render
from django.http import HttpResponse

from .forms import  WorkOrderForm

# Create your views here.
def create_work_order(request):
	if request.method == 'POST':
		return HttpResponse("Received form")
	else:
		form = WorkOrderForm()

	return render(request, 'workorder/create_work_order.html', {'form': form})