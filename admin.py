from django.contrib import admin
from myapp.models import *

# Register your models here.

@admin.register(EmployeeDetailmodel)
class EmployeeDetailadmin(admin.ModelAdmin):
    list_display = ['user', 'contact', 'role', 'technology'] 

@admin.register(Timemodel)
class Timeadmin(admin.ModelAdmin):
    list_display = ['employee', 'date_field', 'working_hour', 'start_time', 'end_time', 'break_duration']

@admin.register(Leavemodel)
class Leaveadmin(admin.ModelAdmin):
    list_display = ['employee', 'leave_type', 'from_date', 'to_date'] 
