from __future__ import unicode_literals

from django.db import models
from employee.models import Employee #   
from customer.models import Customer #
from vehicle.models import Vehicle   #
# Create your models here.
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
	customer 	 		= models.ForeignKey('Customer', on_delete=models.CASCADE)
	vehicle             = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
	employee            = models.ForeignKey('Employee', on_delete=models.CASCADE)
	odometer            = models.IntegerField()
	date_created        = models.DateTimeField() 
	problem_description = models.CharField(max_length=400)
	estimate_initial    = models.FloatField(choices=Initial_Estimate)
	service_type        = models.CharField(max_length=100)
	estimate_revision   = models.FloatField()
	hours_required      = models.FloatField()
	parts_require		= models.CharField(max_length=200, null=true)
	estimate_approval   = models.CharField(max_length=100)
	approval_date_time  = models.DateTimeField()
	amount_paid         = models.FloatField()
	date_completed      = DateTimeField()

	def __str__(self):
		return self.customer + " " + self.vehicle + self.employee





