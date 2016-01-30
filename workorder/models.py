from __future__ import unicode_literals

from django.db import models
from employee.models import Employee #   
from customer.models import Customer #
from vehicle.models  import Vehicle  #
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
	customer 	 		= models.ForeignKey(Customer, on_delete=models.CASCADE)
	vehicle             = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	employee            = models.ForeignKey(Employee, on_delete=models.CASCADE)
	odometer            = models.IntegerField()
	date_created        = models.DateTimeField() 
	problem_description = models.CharField(max_length=400)
	service_type        = models.ManyToManyField('ServiceType')
	estimate_initial    = models.IntegerField(blank=True)
	estimate_revision   = models.FloatField(blank=True)
	hours_required      = models.FloatField()
	parts_require		= models.CharField(max_length=200, blank=True)
	estimate_approval   = models.CharField(max_length=100, blank=True)
	approval_date_time  = models.DateTimeField(blank=True)
	amount_paid         = models.FloatField(blank=True)
	date_completed      = models.DateTimeField(blank=True)

	class Meta:
		db_table = "CKTM_WORKORDER"

	#def __str__(self):
	#	return self.customer + " " + self.vehicle + self.employee

class ServiceType(models.Model):
	name = models.CharField(max_length=100)
	cost = models.FloatField()

	def __str__(self):
		return self.name + " " + str(self.cost)



