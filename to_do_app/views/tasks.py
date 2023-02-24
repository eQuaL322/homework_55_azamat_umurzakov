from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from to_do_app.forms import TaskForm
from to_do_app.models import Task, StatusChoice


def add_task(request: WSGIRequest):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'add_new_task.html', context={
            'choices': StatusChoice.choices,
            'form': form
        })

    form = TaskForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'add_new_task.html', context={
            'choices': StatusChoice.choices,
            'form': form
        })

    else:
        article = Task.objects.create(**form.cleaned_data)
        return redirect('task_view', pk=article.pk)


def update_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.description = request.POST.get('description')
        task.detailed_description = request.POST.get('detailed_description')
        task.status = request.POST.get('status')
        task.complete_data = request.POST.get('complete_data')
        task.save()
        return redirect('task_view', pk=task.pk)
    return render(request, 'task_update.html', context={
        'task': task,
        'choices': StatusChoice.choices
    })
