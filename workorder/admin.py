from django.contrib import admin
from .models import WorkOrder, ServiceType, Part, EmployeeServiceNotes
# Register your models here.
admin.site.register(WorkOrder)
admin.site.register(ServiceType)
admin.site.register(Part)
admin.site.register(EmployeeServiceNotes)