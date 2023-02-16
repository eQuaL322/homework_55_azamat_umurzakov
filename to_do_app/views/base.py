from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404

from to_do_app.models import Task


def tasks_list(request: WSGIRequest):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'task_list.html', context=context)


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={
        'task': task
    })
