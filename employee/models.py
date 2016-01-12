from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
	first_name = models.CharField(max_length=200)
	middle_initial = models.CharField(max_length=1)
	last_name = models.CharField(max_length=200)
	job_title = models.ForeignKey('Job')
	wage = models.FloatField()
	birthdate = models.DateField()
	sex		= models.BooleanField()

	def __str__(self):
		return self.first_name, self.last_name



class Job(models.Model):
	title = models.CharField(max_length=200)