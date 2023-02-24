from django.urls import path

from to_do_app.views.base import tasks_list, task_view
from to_do_app.views.tasks import add_task, update_task_view

urlpatterns = [
    path('', tasks_list, name='task_list'),
    path('task/<int:pk>', task_view, name='task_view'),
    path('task/add', add_task, name='task_add'),
    path('task/<int:pk>/update/', update_task_view, name='update_task_view'),
]
