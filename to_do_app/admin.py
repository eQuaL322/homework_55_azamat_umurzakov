from django.contrib import admin

from to_do_app.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status', 'complete_data', 'detailed_description')
    list_filter = ('id', 'description', 'status', 'complete_data')
    search_fields = ('description', 'status', 'detailed_description')
    fields = ('description', 'status', 'complete_data', 'detailed_description')


admin.site.register(Task, TaskAdmin)
