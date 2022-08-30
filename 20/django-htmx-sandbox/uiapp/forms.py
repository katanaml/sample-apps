from django import forms
from .models import EmployeeModel


class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if '@' not in email:
            raise forms.ValidationError('Invalid email')
        return email

    def clean_salary(self):
        salary = self.cleaned_data['salary']
        if salary < self.cleaned_data['job_id'].min_salary or salary > self.cleaned_data['job_id'].max_salary:
            raise forms.ValidationError(
                'Invalid salary, must be in range [{}, {}]'.format(self.cleaned_data['job_id'].min_salary,
                                                                   self.cleaned_data['job_id'].max_salary))
        return salary

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
