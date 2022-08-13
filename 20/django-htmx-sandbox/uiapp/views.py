from django.shortcuts import render
from django.views.generic import ListView
from .models import EmployeeModel
from .forms import EmployeeForm


class EmployeeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        employees = EmployeeModel.objects.all()
        context = {'employees': employees}
        return render(request, self.template_name, context)


class EmployeeEditView(ListView):
    template_name = 'edit-form-htmx.html'
    view_template_name = 'view-table-htmx.html'

    def get(self, request, pk):
        employee = EmployeeModel.objects.get(pk=pk)
        form = EmployeeForm(instance=employee)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        # handle save after edit
        if request.POST.get('id') is not None:
            pk = request.POST.get('id')

        employee = EmployeeModel.objects.get(pk=pk)
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            print(pk)
            print(form.cleaned_data)

            form.save()

            employees = EmployeeModel.objects.all()
            return render(request, self.view_template_name, {'employees': employees})

        context = {'form': form}
        return render(request, self.template_name, context)

