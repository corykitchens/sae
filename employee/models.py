from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
	JOB_TITLES = (
		('Management', 'mgmt'),
		('Administrative', 'admin'),
		('Service Technician', 'tech')
	)
	SEX_CHOICES = (
		('m', 'Male'),
		('f', 'Female')
	)
	ssn = models.IntegerField(unique=True)
	first_name = models.CharField(max_length=200)
	middle_initial = models.CharField(max_length=1, blank=True, null=False)
	last_name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200, unique=True, null=True, blank=True)
	job_title = models.CharField(max_length=200, choices=JOB_TITLES)
	wage = models.FloatField()
	birthdate = models.DateField(null=True)
	sex	= models.CharField(max_length=10, choices=SEX_CHOICES)
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		related_name="useraccount",
		null=True
		)
	

	class Meta:
		db_table = "CKTM_EMPLOYEE"
		ordering = ['-job_title']

	def __str__(self):
		return self.first_name + " " + self.last_name

	def save(self, *args, **kwargs):
		if self.email is None:
			self.email = self.first_name[0] + self.last_name + "@stockdaleautoelec.com"
		elif self.user is None:
			username = self.first_name[0] + self.last_name
		super(Employee, self).save(*args, **kwargs)
		


class EmployeeAddress(models.Model):

	STATES = (
			 (	'Alabama'	    ,	'AL'), (	'Alaska'	    ,	'AK'),
			 (	'Arizona'	    ,	'AZ'), (	'Arkansas'	    ,	'AR'),
			 (	'California'    ,   'CA'), (	'Colorado'	    ,	'CO'),
			 (	'Connecticut'   ,   'CT'), (	'Delaware'	    , 	'DE'),
			 (	'Florida'	    ,	'FL'), (	'Georgia'	    ,	'GA'),
			 (	'Hawaii'	    ,	'HI'), (	'Idaho'	        ,	'ID'),
			 (	'Illinois'	    ,	'IL'), (	'Indiana'	    ,	'IN'),
			 (	'Iowa'	        ,	'IA'), (	'Kansas'	    ,	'KS'),
			 (	'Kentucky'	    ,	'KY'), (	'Louisiana'	    ,	'LA'),
			 (	'Maine'	        ,	'ME'), (	'Maryland'	    ,	'MD'),
			 (	'Massachusetts'	,	'MA'), (	'Michigan'	    ,	'MI'),
			 (	'Minnesota'	    ,	'MN'), (	'Mississippi'	,	'MS'),
			 (	'Missouri'	    ,	'MO'), (	'Montana'	    ,	'MT'),
			 (	'Nebraska'	    ,	'NE'), (	'Nevada'        ,	'NV'),
			 (	'New Hampshire'	,	'NH'), (	'New Jersey'	,	'NJ'),
			 (	'New Mexico'	,	'NM'), (	'New York'	    ,	'NY'),
			 (	'North Carolina',	'NC'), (	'North Dakota'	,	'ND'),
			 (	'Ohio'	        ,	'OH'), (	'Oklahoma'	    ,	'OK'),
			 (	'Oregon'	    ,	'OR'), (	'Pennsylvania'	,	'PA'),
			 (	'Rhode Island'	,	'RI'), (	'South Carolina',	'SC'),
			 (	'South Dakota'	,	'SD'), (	'Tennessee'	    ,	'TN'),
		     (	'Texas'	        ,	'TX'), (	'Utah'	        ,	'UT'),
			 (	'Vermont'	    ,	'VT'), (	'Virginia'	    ,	'VA'),
			 (	'Washington'	,	'WA'), (	'West Virginia'	,	'WV'),
			 (	'Wisconsin'	    ,	'WI'), (	'Wyoming'	    ,	'WY'),
		)

	address  = models.CharField   (max_length=200)
	city     = models.CharField   (max_length=50)
	state    = models.CharField   (max_length=50, choices=STATES)
	zip_code = models.IntegerField()
	employee = models.ForeignKey(Employee)

	class Meta:
		db_table = "CKTM_EmployeeAddress"

	def full_address(self):
		return self.address + " " + self.city + " " + self.state + " " + str(self.zip_code)
	def __str__(self):
		return self.address + " " + self.city + " " + self.state + " " + str(self.zip_code)


