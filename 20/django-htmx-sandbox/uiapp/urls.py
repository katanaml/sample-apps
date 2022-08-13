from django.urls import path, include
from .views import EmployeeListView, EmployeeEditView


urlpatterns = [
    path('', EmployeeListView.as_view(), name='index'),
    path('edit_employee/<int:pk>/', EmployeeEditView.as_view(), name='edit_employee'),
    path("__reload__/", include("django_browser_reload.urls")),
]