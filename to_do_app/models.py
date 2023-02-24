from django.db import models
from django.db.models import TextChoices


class StatusChoice(TextChoices):
    NEW = 'NEW', 'Новая'
    IN_PROCESS = 'IN_PROCESS', 'В процессе'
    COMPLETE = 'COMPLETE', 'Сделано'


class Task(models.Model):
    description = models.TextField(max_length=100, blank=False, verbose_name="Описание")
    detailed_description = models.TextField(max_length=2000, blank=True, verbose_name="Подробное описание")
    status = models.CharField(verbose_name="Статус", choices=StatusChoice.choices, max_length=20,
                              default=StatusChoice.NEW)
    complete_data = models.DateField(blank=True, null=True, verbose_name="Дата выполнения")

    def __str__(self):
        return f"{self.description} {self.status}"
