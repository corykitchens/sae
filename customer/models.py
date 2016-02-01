from django.db import models
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField

class Customer_Address(models.Model):
    address  = models.CharField(max_length=80)
    city	 = models.CharField(max_length=80)
    state 	 = models.CharField(max_length=80)
    zip_code = models.IntegerField(default=93313)
    slug = models.SlugField(blank=True)
    class Meta:
        verbose_name_plural = 'customer_address'
    def __unicode__(self):
        return u"%s" % self.address
    def save(self, *args, **kwargs):
        self.slug = slugify(self.address)
        return super(Customer_Address, self).save(*args, **kwargs)
    @models.permalink
    def get_absolute_url(self):
        return ('customer_detail', [self.slug])
    @models.permalink
    def get_update_url(self):
        return ('customer_address_update', [self.slug])
    @models.permalink
    def get_delete_url(self):
        return ('customer_address_delete', [self.slug])

class Customer(models.Model):
    first_name     = models.CharField(max_length=60, help_text='Their first name')
    middle_initial = models.CharField(max_length=1, null=True, blank=True)
    last_name      = models.CharField(max_length=80, blank=True, help_text='Their last name')
    slug 	       = models.SlugField(blank=True)
    address        = models.ForeignKey(Customer_Address, blank=True, null=True, help_text='What is the address?')
    home_phone     = PhoneNumberField(blank=True)
    cell_phone     = PhoneNumberField(blank=True)
    email          = models.EmailField(blank=True, null=True, help_text='Do they have an Email address?')

    class Meta:
        verbose_name_plural = 'customer'
        ordering = ['last_name']
    @property
    def full_name(self):
        return u"%s %s" % (self.first_name, self.last_name) if self.last_name != '' else u"%s" % self.first_name
    def __unicode__(self):
        return u"%s, %s" % (self.last_name, self.first_name) if self.last_name != '' else u"%s" % self.first_name
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