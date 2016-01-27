from __future__ import unicode_literals

from django.db import models

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

	address  = models.CharField   (max_length=200)
	city     = models.CharField   (max_length=50)
	state    = models.CharField   (max_length=50, choices=STATES)
	zip_code = models.IntegerField()

	class Meta:
		db_table = "CKTM_CUSTOMER_ADDRESS"

	def full_address(self):
		return self.address + " " + self.city + " " + self.state + " " + self.zip_code
	def __str__(self):
		return self.address + " " + self.city + " " + self.state + " " + self.zip_code