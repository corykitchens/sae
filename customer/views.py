from __future__ import print_function
import sys
import json
from io import BytesIO, StringIO
import StringIO
from reportlab.pdfgen import canvas
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from cgi import escape

import random
#from customer.reports import MyReport
#from customer.reports import MyReport
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from workorder.models import WorkOrder, Part, EmployeeServiceNotes
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Count
from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from customer.forms import CustomerForm, AddressForm, Customer_Edit_Form, Address_Edit_Form
from customer.models import Customer, Customer_Address
from vehicle.models import Vehicle
from django.http import HttpResponse

from easy_pdf.views import PDFTemplateView
from easy_pdf.rendering import render_to_pdf_response
from . import mycharts

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def barchart(request):
    #instantiate a drawing object
    import mycharts
    d_to = request.GET['date_to']
    d_from = request.GET['date_from']
    dates = dict()
    dates = {
        'to' : d_to,
        'from' : d_from
    }

    d = mycharts.Bar(date_to=d_to, date_from=d_from)

    #extract the request params of interest.
    #I suggest having a default for everything.
    if 'height' in request:
        d.height = int(request['height'])
    if 'width' in request:
        d.width = int(request['width'])
    
    if 'numbers' in request:
        strNumbers = request['numbers']

        numbers = map(int, strNumbers.split(','))    
        #d.chart.data = [numbers]   #bar charts take a list-of-lists for data

    if 'title' in request:
        d.title.text = request['title']
  

    #get a GIF (or PNG, JPG, or whatever)
    binaryStuff = d.asString('gif')
    response_data = dict()
    response_data['img'] = binaryStuff
    return HttpResponse(binaryStuff, 'image/gif')

#Publisher.objects.filter(name__contains="press") --- How to filter objects by a string regardless of length
def CustomerDirectory(request):
    customer_list = Customer.objects.all()
    paginator = Paginator(customer_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        customers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        customers = paginator.page(paginator.num_pages)
    return render(request, 'customer/customer_list.html', {'customers': customers})

# choice has the foreign key choice is customer poll is address
def add(request):
    CustomerFormSet = formset_factory(CustomerForm, extra=1, min_num=0,validate_min=True)
    if request.method == 'POST':
        customer_address_form = AddressForm(request.POST)
        customer_form = CustomerFormSet(request.POST)
        if all([customer_form.is_valid(), customer_address_form.is_valid()]):
            address = customer_address_form.save()
            for inline_form in customer_form:
                if inline_form.cleaned_data:
                    customer = inline_form.save(commit=False)
                    customer.address = address
                    customer.save()
            return redirect('customer_directory.html', {})
    else:
        form = AddressForm()
        formset = CustomerFormSet()

    return render(request, 'customer/customer_form.html', {'formset': formset, 'form': form})

def customer_profile(request, customer_id):
    customer  = Customer.objects.get(id=customer_id)
    return render(request, 'customer/customer_profile.html', {'customer': customer})

def vehicle_profile(request, vehicle_id):
    vehicle         = Vehicle.objects.get(pk=vehicle_id)
    workorder = WorkOrder.objects.filter(vehicle=vehicle)
    return render(request, 'customer/vehicle_profile.html', {'vehicle': vehicle, 'workorder': workorder} )

def workorder_summary(request, workorder_id):
    workorder = WorkOrder.objects.get(id=workorder_id)
    service_notes = EmployeeServiceNotes.objects.filter(work_order=workorder_id)
    return render(request,'customer/workorder_summary.html', {'workorder': workorder, 'service_notes' : service_notes})    

def pdf_workorder_summary(request, workorder_id):
    workorder = WorkOrder.objects.get(id=workorder_id)
    return render_to_pdf('customer/pdf_workorder_summary.html', {'workorder': workorder})    
        
def piechart(request):
    # Initialise the report
    template = "myapp/my_report.html"
    report = MyReport()
    context = {'report': report}

    return render(request, template, context)

def print_objs(*objs):
    print("OUTPUT->", objs, file=sys.stderr)

def edit(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    Customer_EditFormSet = formset_factory(Customer_Edit_Form, extra=1, min_num=0,validate_min=True)
    if request.method == 'POST':
        address_edit_form = Address_Edit_Form(request.POST)
        customer_edit_form = Customer_EditFormSet(request.POST)
        if all([customer_edit_form.is_valid(), address_edit_form.is_valid()]):
            address = address_edit_form.save()
            for inline_form in customer_edit_form:
                if inline_form.cleaned_data:
                    customer.address = address
                    customer.save()
            return redirect('/customers/customer_directory', {})
    else:
        form = Address_Edit_Form()
        formset = Customer_EditFormSet()

    return render(request, 'customer/customer_edit_form.html', {'formset': formset, 'form': form})


def generate_history(request, vehicle_id):
    date_from = request.GET['date_from']
    date_to = request.GET['date_to']
    dates = dict()
    dates['from'] = date_from
    dates['to'] = date_to

    try:
        w = WorkOrder.objects.filter(vehicle=vehicle_id)
    except WorkOrder.DoesNotExist:
        return HttpResponse('No Work Orders')
    try:
        workorder = WorkOrder.objects.filter(vehicle=vehicle_id, date_created__gt=date_from, date_created__lt=date_to)
    except WorkOrder.DoesNotExit:
        return HttpResponse('Query didnt work')
    return render(request,'customer/workorder_summary_history.html', {'dates': dates, 'workorder': workorder})    

def pdf_history_summary(request, vehicle_id):
    date_from = request.GET['date_from']
    date_to = request.GET['date_to']
    dates = dict()
    dates['from'] = date_from
    dates['to'] = date_to

    try:
        w = WorkOrder.objects.filter(vehicle=vehicle_id)
    except WorkOrder.DoesNotExist:
        return HttpResponse('No Work Orders')
    try:
        workorder = WorkOrder.objects.filter(vehicle=vehicle_id, date_created__gt=date_from, date_created__lt=date_to)
    except WorkOrder.DoesNotExit:
        return HttpResponse('Query didnt work')
    return render_to_pdf('customer/workorder_summary_history.html', {'dates': dates, 'workorder': workorder})    


def get_customer(request, first_name, last_name):
    response_data = dict()
    try:
        customer = Customer.objects.get(first_name=first_name.capitalize(), last_name=last_name.capitalize())
    except Customer.DoesNotExist:
        response_data['msg'] = 'Error querying customer'
        return HttpResponse(json.dumps(response_data),content_type="application/json") 

    
    response_data['customer_fn'] = customer.first_name
    response_data['customer_ln'] = customer.last_name
    response_data['customer_mi'] = customer.middle_initial
    response_data['customer_email'] = customer.email
    response_data['customer_address'] = customer.address.address
    response_data['customer_city'] = customer.address.city
    response_data['customer_state'] = customer.address.state
    response_data['customer_zip_code'] = customer.address.zip_code
    try:
        customer_vehicles = customer.vehicle.all() 
    except Vehicle.DoesNotExist:
        response_data['customer_vehicles'] = {}

    serialized_vehicles = serializers.serialize("json", customer.vehicle.all())
    response_data['customer_vehicles'] = serialized_vehicles

    return HttpResponse(json.dumps(response_data),
            content_type="application/json"
)


def reports(request):
    return render(request, 'customer/report.html', {})


def generate_report(request):
    date_from = request.GET['date_from']
    date_to = request.GET['date_to']
    dates = dict()
    dates['from'] = date_from
    dates['to'] = date_to

    try:
        workorders = WorkOrder.objects.filter(date_created__gte=date_from, date_created__lte=date_to).order_by('date_created')
    except WorkOrder.DoesNotExit:
        return HttpResponse('Query didnt work')

    
    response_data = dict()
    workorder_cost = list()
    workorder_date = list()


    from_month = int(date_from[6])
    to_month = int(date_to[6])
    list_of_months = ['January','February','March','April','May','June','July','August', 'September', 'October', 'November', 'December']
    response_data['w_date'] = list_of_months[from_month-1:to_month]


    sales      = [0,0,0,0,0,0,0,0]
    sales_goal = [9000, 8000, 9200, 10200, 16000, 20000, 22000, 20000, 20000, 16000, 11000, 6000]
    net_sales = list()
    project_sales = list()
    for i in range(from_month-1, to_month):
        workorders = WorkOrder.objects.filter(date_created__month=i+1)
        total_cost = 0
        project_sales.append(sales_goal[i])
        for workorder in workorders:
            total_cost = total_cost + workorder.estimate_revision
            net_sales.append(workorder.estimate_revision - sales[i]*.34)
            
        workorder_cost.append(total_cost)
        
    response_data['w_projections'] = project_sales
    response_data['w_net_sales'] = net_sales
    response_data['w_cost'] = workorder_cost

    return HttpResponse(json.dumps(response_data), content_type='application/json')
