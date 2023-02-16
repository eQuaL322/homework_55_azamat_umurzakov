from django.contrib import admin

from to_do_app.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status', 'complete_data')
    list_filter = ('id', 'description', 'status', 'complete_data')
    search_fields = ('description', 'status')
    fields = ('description', 'status', 'complete_data')


admin.site.register(Task, TaskAdmin)
