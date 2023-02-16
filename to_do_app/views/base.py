from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from to_do_app.models import Task


def tasks_list(request: WSGIRequest):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'task_list.html', context=context)


def task_view(request):
    task_pk = request.GET.get('pk')
    task = Task.objects.get(pk=task_pk)
    context = {
        'task': task
    }
    return render(request, 'task.html', context=context)
