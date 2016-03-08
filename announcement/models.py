from __future__ import unicode_literals
import datetime

from django.db import models

from employee.models import Employee
# Create your models here.
class Announcement(models.Model):
	title = models.CharField(max_length=50)
	body = models.TextField(max_length=300)
	posted = models.DateField(default=datetime.date.today())
	posted_by = models.ForeignKey(Employee)

	class Meta:
		db_table="CKTM_ANNOUNCEMENT"
		ordering=['posted']