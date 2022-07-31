from django.urls import path
from .views import display_tasks, delete_task

urlpatterns = [
    path('tasks/', display_tasks, name='display_tasks'),
    path('tasks/<int:task_id>/delete/', delete_task, name='delete_task'),
]