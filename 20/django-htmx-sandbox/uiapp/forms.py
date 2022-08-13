from django import forms
from .models import EmployeeModel


class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = ['employee_id',
                  'first_name',
                  'last_name',
                  'email',
                  'phone_number',
                  'hire_date',
                  'job_id',
                  'salary',
                  'commission_pct',
                  'manager_id',
                  'department_id']
        widgets = {
            'hire_date': DateInput()
        }
