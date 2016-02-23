from __future__ import unicode_literals

from django.db import models
from vehicle.models import Vehicle

# Create your models here.
class Customer_Address(models.Model):

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
	
	address  = models.CharField   (max_length=200, default='', null=True)
	city     = models.CharField   (max_length=50, default='Bakersfield', null=True)
	state    = models.CharField   (max_length=50, choices=STATES, default='California', null=True)
	zip_code = models.IntegerField(default=93304, null=True)
	

	class Meta:
		db_table = "CKTM_CUSTOMER_ADDRESS"

	def full_address(self):
		return str(self.address + " " + self.city + " " + self.state)

	def __str__(self):
		return unicode(self.address + " " + self.city + " " + self.state) or u''

class Customer(models.Model):

	
	first_name     = models.CharField(max_length=200)
	middle_initial = models.CharField(max_length=1, blank=True)
	last_name      = models.CharField(max_length=200)
	email          = models.EmailField(max_length=200, null=True, blank=True)
	address  	   = models.ForeignKey(Customer_Address, null=True)
	vehicle 	   = models.ManyToManyField(Vehicle)

	class Meta:
		db_table = "CKTM_CUSTOMER"

	def full_name(self):
		return self.first_name + " " + self.last_name
	def __str__(self):
		return self.first_name + " " + self.last_name


