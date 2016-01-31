from __future__ import unicode_literals
from django.template.defaultfilters import slugify
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
	slug     = models.SlugField(blank=True)

	class Meta:
		db_table = "CKTM_CUSTOMER_ADDRESSES"
		verbose_name_plural = 'customer_address'

	def full_address(self):
		return self.address + " " + self.city + " " + self.state + " " + self.zip_code
	def __str__(self):
		return self.address + " " + self.city + " " + self.state + " " + self.zip_code

	 
     
    def __unicode__(self):
        return u"%s" % self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Customer_Address, self).save(*args, **kwargs)

	    @models.permalink
    def get_absolute_url(self):
        return ('customer_address_detail', [self.slug])
    @models.permalink
    def get_update_url(self):
        return ('customer_address_update', [self.slug])
    @models.permalink
    def get_delete_url(self):
        return ('customer_address_delete', [self.slug])

class Customer(models.Model):

	first_name     = models.CharField(max_length=200)
	middle_initial = models.CharField(max_length=1)
	last_name      = models.CharField(max_length=200)
	email          = models.EmailField(max_length=200, blank=True, unique=True, null=True)
	address        = models.ForeignKey(Customer_Address, blank=True, null=True)
	slug 		   = models.SlugField(blank=True)

	class Meta:
		db_table = "CKTM_CUSTOMER"

	class Meta:
        verbose_name_plural = 'customer'
        ordering = ['last_name']
    @property
    def full_name(self):
        return u"%s %s" % (self.first_name, self.last_name, self.middle_initial) if self.last_name != '' else u"%s" % self.first_name
    def __unicode__(self):
        return u"%s, %s" % (self.last_name,  self.first_name, self.middle_initial) if self.last_name != '' else u"%s" % self.first_name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.full_name)
        return super(Customer, self).save(*args, **kwargs)
    @models.permalink
    def get_absolute_url(self):
        return ('customer_detail', [self.slug])
    @models.permalink
    def get_update_url(self):
        return ('customer_update', [self.slug])
    @models.permalink
    def get_delete_url(self):
        return ('customer_delete', [self.slug])


