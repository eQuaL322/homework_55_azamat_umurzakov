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
    errors = {}
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if not form.is_valid():
            errors = form.errors
        else:
            task.description = form.cleaned_data['description']
            task.detailed_description = form.cleaned_data['detailed_description']
            task.status = form.cleaned_data['status']
            task.complete_data = form.cleaned_data['complete_data']
            task.save()
            return redirect('task_view', pk=task.pk)
    else:
        form = TaskForm(initial={
            'description': task.description,
            'detailed_description': task.detailed_description,
            'status': task.status,
            'complete_data': task.complete_data,
        })
    return render(request, 'task_update.html', context={
        'form': form,
        'task': task,
        'choices': StatusChoice.choices,
        'errors': errors,
    })


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_confirm_delete.html', context={'task': task})


def confirm_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={
        'task': task
    })
