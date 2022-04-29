from django.urls import path
from .views import EmployeeList, EmployeeDetail, EmployeeCreate, EmployeeUpdate, EmployeeDelete, CustomLoginView
from .views import RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', EmployeeList.as_view(), name='employees'),
    path('employee/<int:pk>/', EmployeeDetail.as_view(), name='employee'),
    path('employee-create/', EmployeeCreate.as_view(), name='employee-create'),
    path('employee-update/<int:pk>/', EmployeeUpdate.as_view(), name='employee-update'),
    path('employee-delete/<int:pk>/', EmployeeDelete.as_view(), name='employee-delete'),
]