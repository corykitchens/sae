from django.conf.urls import url
from announcement.views import get_all_announcements


urlpatterns = [
	url('all', get_all_announcements, name='all')
]