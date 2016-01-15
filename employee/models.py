from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
	JOB_TITLES = (
		('mgmt', 'Management'),
		('admin', 'Administrative'),
		('tech', 'Service Technician')
	)
	SEX_CHOICES = (
		('m', 'Male'),
		('f', 'Female')
	)
	ssn = models.IntegerField(primary_key=True)
	first_name = models.CharField(max_length=200)
	middle_initial = models.CharField(max_length=1)
	last_name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200, unique=True, null=True)
	job_title = models.CharField(max_length=200, choices=JOB_TITLES)
	wage = models.FloatField()
	birthdate = models.DateField(null=True)
	sex	= models.CharField(max_length=10, choices=SEX_CHOICES)

	

	class Meta:
		db_table = "CKTM_EMPLOYEE"

	def __str__(self):
		return self.first_name + " " + self.last_name
