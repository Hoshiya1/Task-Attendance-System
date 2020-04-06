from django.contrib import admin

# Register your models here.
from .models import Emp, Dept

class EmpAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name', 'email', 'phone', 'sex', 'dept_id', 'leader_id']

class DeptAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name']

admin.site.register(Emp, EmpAdmin)
admin.site.register(Dept, DeptAdmin)
