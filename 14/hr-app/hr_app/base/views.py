from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Employee


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('employees')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('employees')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('employees')
        return super(RegisterPage, self).get(*args, **kwargs)


class EmployeeList(LoginRequiredMixin, ListView):
    model = Employee
    context_object_name = 'employees'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = context['employees'].filter(user=self.request.user)
        context['count'] = context['employees'].filter(approved=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['employees'] = context['employees'].filter(lastName__istartswith=search_input)

        context['search_input'] = search_input

        return context


class EmployeeDetail(LoginRequiredMixin, DetailView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'base/employee.html'


class EmployeeCreate(LoginRequiredMixin, CreateView):
    model = Employee
    fields = ['firstName', 'lastName', 'approved']
    success_url = reverse_lazy('employees')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EmployeeCreate, self).form_valid(form)


class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = ['firstName', 'lastName', 'approved']
    success_url = reverse_lazy('employees')


class EmployeeDelete(LoginRequiredMixin, DeleteView):
    model = Employee
    context_object_name = 'employee'
    success_url = reverse_lazy('employees')
