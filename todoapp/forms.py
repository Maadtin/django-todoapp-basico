from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'text',
            'done'
        ]
        labels = {
            'text': 'Nombre de la tarea',
            'done': 'Tarea acabada'
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({
            'class': 'form-control'
        })
