from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from to_do_app.models import Task


def add_task(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'add_new_task.html')
    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status', 'new'),
        'complete_data': request.POST.get('complete_data'),
        'detailed_description': request.POST.get('detailed_description')
    }
    status_mapping = {
        'new': 'новая',
        'in_process': 'в процессе',
        'complete': 'сделано',
    }
    task_data['status'] = status_mapping.get(task_data['status'], 'new')
    task = Task.objects.create(**task_data)

    return redirect('task_view', pk=task.pk)
