from django.contrib import admin
from .models import EmployeeModel, JobModel, DepartmentsModel


admin.site.register(EmployeeModel)
admin.site.register(JobModel)
admin.site.register(DepartmentsModel)