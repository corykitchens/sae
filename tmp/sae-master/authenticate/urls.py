from django.conf.urls import url
from . import views

app_name="authenticate"

urlpatterns = [
	url(r'^logout', views.logout),
	url(r'^$', views.login, name='login'),
	
]