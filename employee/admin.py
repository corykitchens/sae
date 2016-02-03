from django.contrib import admin
from .models import Employee, EmployeeAddress
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	exclude=('email', 'user')
admin.site.register(EmployeeAddress)