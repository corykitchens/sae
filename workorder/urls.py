from django.conf.urls import url

from .views import create_work_order

urlpatterns = [
	url(r'^', create_work_order, name="create_work_order")
]