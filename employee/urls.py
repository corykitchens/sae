from django.conf.urls import url

from employee.views import EmployeeDirectory, employee_profile
from . import views
urlpatterns = [
	#landing page
	url(r'^employee_directory', EmployeeDirectory.as_view(), name="employee_index"),
	url(r'^edit_profile/(?P<employee_id>[0-9])$', employee_profile, name="employee_profile")	
	# r'^ <- begin of raw string
	# $' <- end of raw string
	#url(r'^(?P<test>[a-z]{2})$', views.a)



]