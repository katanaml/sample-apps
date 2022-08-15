from django.db import models


class JobModel(models.Model):
    job_id = models.CharField(primary_key=True, max_length=10)
    job_title = models.CharField(max_length=35)
    min_salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    max_salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ['-job_id']


class DepartmentsModel(models.Model):
    department_id = models.SmallIntegerField(primary_key=True)
    department_name = models.CharField(max_length=30)
    manager_id = models.ForeignKey('EmployeeModel', on_delete=models.CASCADE, blank=True, null=True)
    location_id = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        ordering = ['-department_id']


class EmployeeModel(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    hire_date = models.DateField()
    job_id = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    commission_pct = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    manager_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    department_id = models.ForeignKey(DepartmentsModel, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['-employee_id']
        constraints = [
            models.CheckConstraint(check=models.Q(salary__gte=0), name='salary_constraint', violation_error_message='Salary must be greater than 0'),
            models.UniqueConstraint(fields=['email'], name='Email must be unique'),
        ]