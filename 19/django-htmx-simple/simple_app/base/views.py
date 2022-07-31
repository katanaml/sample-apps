from django.shortcuts import render
from .models import TaskModel
from django.views.decorators.http import require_http_methods


def display_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'display_tasks.html', {'tasks': tasks})


@require_http_methods(['DELETE'])
def delete_task(request, task_id):
    TaskModel.objects.filter(id=task_id).delete()
    tasks = TaskModel.objects.all()
    return render(request, 'tasks_list.html', {'tasks': tasks})
