from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Vehicle(models.Model):
	license_plate = models.CharField(max_length=20)
	make          = models.CharField(max_length=20)
	model         = models.CharField(max_length=20)
	vin           = models.CharField(max_length=20)
	year          = models.DateField()

	class Meta:
		db_table = "CKTM_VEHICLE"

	def vehicle_info(self):
		return slef.year + " " + self.make + " " + self.model + " " + self.license_plate
	def __str__(self):
		return slef.year + " " + self.make + " " + self.model + " " + self.license_plate
