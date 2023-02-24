import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from to_do_app.models import StatusChoice


class TaskForm(forms.Form):
    description = forms.CharField(max_length=100, required=True, label='Заголовок',
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    detailed_description = forms.CharField(max_length=2000, required=False, label="Подробное описание",
                                           widget=widgets.Textarea(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices=StatusChoice.choices, required=True, label="Статус",
                               widget=forms.Select(attrs={'class': 'form-control'}))
    complete_data = forms.DateField(initial=datetime.date.today, required=False, label="Дата выполнения",
                                    widget=forms.DateInput(attrs={'class': 'form-control'}))

    def clean_title(self):
        description = self.cleaned_data.get('description')
        if len(description) < 2:
            raise ValidationError('Заголовок должен быть длиннее 2 символов')
        return description
