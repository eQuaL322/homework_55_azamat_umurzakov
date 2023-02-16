from django.db import models


class Task(models.Model):
    description = models.TextField(max_length=2000, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=200, blank=False, default="new", verbose_name="Статус")
    complete_data = models.DateField(blank=True, null=True, verbose_name="Дата выполнения")
    detailed_description = models.TextField(max_length=2000, blank=True, verbose_name="Подробное описание")

    def __str__(self):
        return f"{self.description} {self.status}"
