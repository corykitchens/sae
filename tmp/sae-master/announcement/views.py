from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_all_announcements(request):
	return HttpResponse('Announcements')