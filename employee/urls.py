from django.conf.urls import url

from employee.views import EmployeeDirectory

urlpatterns = [
	url(r'^', EmployeeDirectory.as_view(), name="employee_index")
]