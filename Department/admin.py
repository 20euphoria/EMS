from atexit import register
from django.contrib import admin
from .models import Department

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['deptid', 'eid', 'deptname']