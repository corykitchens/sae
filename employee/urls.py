from django.conf.urls import url

from employee.views import EmployeeDirectory
from . import views
urlpatterns = [
	#landing page
	url(r'^', EmployeeDirectory.as_view(), name="employee_index"),
	
	# r'^ <- begin of raw string
	# $' <- end of raw string
	#url(r'^(?P<test>[a-z]{2})$', views.a)



]