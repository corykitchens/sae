from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Announcements(models.Model) :
	title       = models.CharField(max_length=100)
	body        = models.CharField(max_length=500)
	date_posted = models.DateTimeField()

	class Meta:
		db_table = "CKTM_ANNOUNCEMENTS"
