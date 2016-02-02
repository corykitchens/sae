from django.conf.urls import url

from employee.views import EmployeeDirectory, employee_profile, hr_home, new_hire
from . import views



urlpatterns = [
	#landing page
	url(r'^employee_directory', EmployeeDirectory.as_view(), name="employee_index"),
	url(r'^edit_profile/(?P<employee_id>[0-9])$', employee_profile, name="employee_profile"),
	url(r'^hr', hr_home, name="hr_home"),
	url(r'^new_hire', new_hire, name="new_hire")
]