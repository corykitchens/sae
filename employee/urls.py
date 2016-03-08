from django.conf.urls import url

from employee.views import *
from . import views



urlpatterns = [
	#landing page
	url(r'^employee_directory', EmployeeDirectory.as_view(), name="employee_index"),
	url(r'^edit_profile/(?P<employee_id>[0-9])', employee_profile, name="employee_profile"),
	url(r'^edit_profile/(?P<employee_id>[0-9])/change_password', views.change_password),
	url(r'^hr', hr_view_pending, name="hr_home"),
	url(r'^new_hire', new_hire, name="new_hire")
]