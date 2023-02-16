from django.urls import path

from to_do_app.views.base import tasks_list, task_view
from to_do_app.views.tasks import add_task

urlpatterns = [
    path('', tasks_list),
    path('task/', task_view),
    path('task/add', add_task)
]
