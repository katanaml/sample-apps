from django.urls import path, include
from .views import IndexView, EmployeeEditView, EmployeeTableView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('employees/', EmployeeTableView.as_view(), name='employees'),
    path('edit_employee/<int:pk>/', EmployeeEditView.as_view(), name='edit_employee'),
    path("__reload__/", include("django_browser_reload.urls")),
]