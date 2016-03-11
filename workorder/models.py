from __future__ import unicode_literals
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils import timezone
from employee.models import Employee #   
from customer.models import Customer #
from vehicle.models  import Vehicle  #
# Create your models here.

@python_2_unicode_compatible
class WorkOrder(models.Model):
	Initial_Estimate = (
		('3-Step Fuel System Service', 139.99), ('Synthetic Oil Change', 75.00),
		('High Mileage Oil Change', 55.00),      ('Star Service Oil Change', 39.99),
		('Coolant Flush', 99.99),                ('Transfer Case Service', 49.99 ),
	    ('Differential Service', 49.99),         ('Automatic Transmission Flush', 99.99),
		('Wiper Blade Replacement, each', 8.99), ('Air Filter Replacement', 15.00),
		('Cabin Air Filter Replacement', 19.99), ('Diagnosis', '105'),
		('AC Service, excludes freon cost', 80.00)
	)

	STATUS_OPTIONS = (
			('Assigned', 'Assigned'),
			('Diagnosing', 'Diagnosing'),
			('Repairing', 'Repairing'),
			('Reassigned', 'Reassigned'),
			('Completed', 'Completed'),
			('Awaiting Payment', 'Awaiting Payment'),
			('Paid in Full', 'Paid in Full' ),
			('Closed', 'Closed'),
			('Cancelled', 'Cancelled')
		)


	customer 	 		= models.ForeignKey(Customer, on_delete=models.CASCADE)
	vehicle             = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	employee            = models.ForeignKey(Employee, on_delete=models.CASCADE)
	odometer            = models.IntegerField()
	date_created        = models.DateTimeField(default=timezone.now()) 
	problem_description = models.CharField(max_length=400)
	service_type        = models.ManyToManyField('ServiceType')
	estimate_initial    = models.FloatField(blank=True)
	estimate_revision   = models.FloatField(blank=True, null=True)
	hours_required      = models.FloatField(blank=True, null=True)
	status 				= models.CharField(null=True, max_length=100, choices=STATUS_OPTIONS)
	parts_required		= models.CharField(null=True,max_length=200, blank=True)
	estimate_approval   = models.NullBooleanField(null=True)
	approval_date_time  = models.DateTimeField(null=True, blank=True)
	amount_paid         = models.FloatField(null=True, blank=True)
	date_completed      = models.DateTimeField(null=True, blank=True)

	class Meta:
		db_table = "CKTM_WORKORDER"

	def __str__(self):
		return str(self.date_created) + " " + str(self.customer) + " " + str(self.vehicle)



@python_2_unicode_compatible
class ServiceType(models.Model):
	name = models.CharField(max_length=100)
	cost = models.FloatField()
	
	def __str__(self):
		return self.name
@python_2_unicode_compatible
class Part(models.Model):
	name = models.CharField(max_length=100)
	cost = models.FloatField()

	def __str__(self):
		return self.name
@python_2_unicode_compatible
class EmployeeServiceNotes(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
	date_serviced = models.DateTimeField()
	hours_spent = models.FloatField()
	notes = models.CharField(max_length=400)
	parts_used = models.ManyToManyField(Part, blank=True, null=True)

	def __str__(self):
		return str(self.date_serviced) + " " + self.employee.first_name + " " + self.employee.last_name





# 
