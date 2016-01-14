from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^', views.employee_index, name="employee_index")
]