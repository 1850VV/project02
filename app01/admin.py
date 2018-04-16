from django.contrib import admin

# Register your models here.
from app01.models import Department, Employee


class DepartmentAdmin(admin.ModelAdmin):
    # 定义要在后台显示哪些字段
    list_display = ['id', 'name', 'create_date']


class EmployeeAdmin(admin.ModelAdmin):
    # 定义要在后台显示哪些字段
    list_display = ['id', 'name', 'age', 'sex', 'salary', 'comment', 'department']


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
