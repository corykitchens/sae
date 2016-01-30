from django.contrib import admin
from .models import WorkOrder, ServiceType
# Register your models here.
admin.site.register(WorkOrder)
admin.site.register(ServiceType)