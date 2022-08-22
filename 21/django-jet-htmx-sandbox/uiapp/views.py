from django.shortcuts import render
from django.views.generic import ListView
from django.core import serializers
from uiapp.models import EmployeeModel


class IndexView(ListView):
    template_name = 'index.html'

    def get(self, request):
        employees = EmployeeModel.objects.all()

        data = serializers.serialize('json', employees, use_natural_foreign_keys=True)

        context = {'employees': data}
        return render(request, self.template_name, context)
