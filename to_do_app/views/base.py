from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from to_do_app.models import Task


def tasks_list(request: WSGIRequest):
    tasks = Task.objects.exclude(is_deleted=True)
    context = {
        'tasks': tasks
    }
    return render(request, 'task_list.html', context=context)
