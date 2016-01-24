from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):

	first_name     = models.CharField(max_length=200)
	middle_initial = models.CharField(max_length=1)
	last_name      = models.CharField(max_length=200)
	#email          = models.EmailField(max_length=200)

	class Meta:
		db_table = "CKTM_CUSTOMER"

	def full_name(self):
		return self.first_name + " " + self.last_name
	def __str__(self):
		return self.first_name + " " + self.last_name


