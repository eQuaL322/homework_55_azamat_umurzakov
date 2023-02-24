from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StatusChoice(TextChoices):
    NEW = 'Новая', 'Новая'
    IN_PROCESS = 'В процессе', 'В процессе'
    COMPLETE = 'Сделано', 'Сделано'


class Task(models.Model):
    description = models.TextField(max_length=100, blank=False, verbose_name="Описание")
    detailed_description = models.TextField(max_length=2000, blank=True, verbose_name="Подробное описание")
    status = models.CharField(verbose_name="Статус", choices=StatusChoice.choices, max_length=20,
                              default=StatusChoice.NEW)
    complete_data = models.DateField(blank=True, null=True, verbose_name="Дата выполнения")
    is_deleted = models.BooleanField(verbose_name="Удалено", null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name="Дата и время удаления", null=True, default=None)

    def __str__(self):
        return f"{self.description} {self.status}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
