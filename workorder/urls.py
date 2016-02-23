from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^create_work_order/$', create_work_order),
	url(r'^$', work_orders, name="workorders"),
	
]