from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^create_work_order/$', create_work_order),
	url(r'^process_payment/(?P<work_order_id>[0-9]+)/', process_payment),
	url(r'^(?P<work_order_id>[0-9]+)/', work_order_detail),
	url(r'^submit_service_notes/', submit_service_notes),
	url(r'^$', work_orders, name="workorders"),


]